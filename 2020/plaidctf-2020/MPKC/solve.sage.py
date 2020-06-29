

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_59 = Integer(59); _sage_const_10 = Integer(10); _sage_const_25 = Integer(25); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_256 = Integer(256); _sage_const_5 = Integer(5); _sage_const_12 = Integer(12); _sage_const_1000 = Integer(1000)# Jiahui Chen et al. cryptosystem, 80-bit security
# WARNING: very slow implementation.
import sys
q,n,a,s = (_sage_const_3 ,_sage_const_59 ,_sage_const_10 ,_sage_const_25 )
m = n+_sage_const_1 -a+s
FF = GF(q)
R = PolynomialRing(FF, ["x{}".format(i) for i in range(n)])
xs = R.gens()

def keygen():
    while True:
        C = random_matrix(FF, n+_sage_const_1 , n)
        if matrix(FF, [_sage_const_2 *C[i]-_sage_const_2 *C[i+_sage_const_1 ] for i in range(n)]).is_invertible():
            break

    FC = []
    for i in range(n+_sage_const_1 ):
        p = _sage_const_0 
        for j in range(n):
            p += (xs[j] - C[i][j])**_sage_const_2 
        FC.append(p)

    while True:
        S_lin = random_matrix(FF, n, n)
        if S_lin.is_invertible():
            break
    S_trans = (FF**n).random_element()
    S = (S_lin, S_trans)

    while True:
        T_lin = random_matrix(FF, m, m)
        if T_lin.is_invertible():
            break
    T_trans = (FF**m).random_element()
    T = (T_lin, T_trans)

    G = []
    for i in range(s):
        G.append(R.random_element(degree=_sage_const_2 , terms=Infinity))
    F = FC[:n+_sage_const_1 -a] + G

    P = vector(xs)
    P = S[_sage_const_0 ]*P
    P += S[_sage_const_1 ]
    v = []
    for i in range(len(F)):
        v.append(F[i](*P))
        print("keygen {}/{}".format(i+_sage_const_1 ,len(F)))
    P = vector(v)
    P = T[_sage_const_0 ]*P
    P += T[_sage_const_1 ]
    print("done keygen")

    return (P, (C, G, S, T))

def make_blocks(ss):
    x = _sage_const_0 
    for i in ss:
        x = x*_sage_const_256 +ord(i)
    v = []
    while x > _sage_const_0 :
        v.append(FF(x%q))
        x = x//q
    v += [FF(_sage_const_0 ) for i in range(n - (len(v) % n))]
    blocks = []
    for i in range(_sage_const_0 , len(v), n):
        blocks.append(vector(v[i:i+n]))
    return blocks

def combine_blocks(blocks):
    x = _sage_const_0 
    for i in blocks[::-_sage_const_1 ]:
        for j in i[::-_sage_const_1 ]:
            x = x*q+Integer(j)
    ss = ""
    while x > _sage_const_0 :
        ss = chr(x % _sage_const_256 ) + ss
        x = x//_sage_const_256 
    return ss

def encrypt_block(plain, pk):
    return vector([pk[i](*plain) for i in range(m)])

def encrypt(plain, pk):
    blocks = make_blocks(plain)
    enc = []
    for i in range(len(blocks)):
        print("encrypt {}/{}".format(i+_sage_const_1 ,len(blocks)))
        enc.append(encrypt_block(blocks[i], pk))
    return enc

def decrypt_block(cipher, sk):
    C, G, S, T = sk
    C2I = matrix(FF, [_sage_const_2 *C[i]-_sage_const_2 *C[i+_sage_const_1 ] for i in range(n)]).inverse()
    cv = []
    for i in range(n):
        cc = _sage_const_0 
        for j in range(n):
            cc += C[i+_sage_const_1 ][j]**_sage_const_2  - C[i][j]**_sage_const_2 
        cv.append(cc)
    cv = vector(cv)
    g1 = T[_sage_const_0 ].inverse()*(cipher - T[_sage_const_1 ])
    for g2 in FF**a:
        print("decrypt: trying:", g2)
        g = vector(list(g1)[:n+_sage_const_1 -a]+list(g2))
        g_diff = vector([g[i+_sage_const_1 ]-g[i] for i in range(len(g)-_sage_const_1 )])
        d = C2I * (g_diff-cv)
        for i,j in zip(G,g1[n+_sage_const_1 -a:]):
            if i(*d) != j:
                break
        else:
            return S[_sage_const_0 ].inverse() * (d - S[_sage_const_1 ])

def decrypt(cipher, sk):
    dec = []
    for i in range(len(cipher)):
        print("decrypt {}/{}".format(i+_sage_const_1 ,len(cipher)))
        dec.append(decrypt_block(cipher[i], sk))
    return combine_blocks(dec)

output = open("output", "rb").read().decode('utf-8').strip().split("\n")
for i in range(n)[::-_sage_const_1 ]:
    output[_sage_const_0 ] = output[_sage_const_0 ].replace("x{}".format(i), "xs[{}]".format(i))
output[_sage_const_0 ] = output[_sage_const_0 ].replace("^", "**")
pk = eval(output[_sage_const_0 ])
flag_cipher = [(_sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 ), (_sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 ), (_sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 ), (_sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 ), (_sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 ), (_sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 )]
print(len(pk))
print(len(flag_cipher))

flag = "PCTF{the_quick_brown_fox}"
# ciph = encrypt(flag, pk)
ciph = [(_sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 ), (_sage_const_2 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 ), (_sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_0 , _sage_const_1 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_0 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_0 , _sage_const_2 , _sage_const_1 , _sage_const_1 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_2 , _sage_const_2 , _sage_const_2 , _sage_const_1 , _sage_const_0 , _sage_const_0 , _sage_const_1 )]
ciph = flag_cipher
block_id = _sage_const_5 
print(ciph)
print(len(ciph))

eqns = [[_sage_const_0  for j in range(m)] for i in range(n*n)]

for i in range(m):
    for x_i in range(n):
        for x_j in range(n):
            eqns[x_i*n + x_j][i] = pk[i].monomial_coefficient(xs[x_i]*xs[x_j])

part1_mat = Matrix(FF, eqns)
kernel_basis = part1_mat.right_kernel(basis='pivot')
print("Basis:", kernel_basis)
sample_basis = kernel_basis.basis()

R = []
for i in range(n-a):
    curr = _sage_const_0 
    for j in range(m):
        curr += sample_basis[i][j] * pk[j]
    R.append(curr)

R_right = []
for i in range(n-a):
    curr = _sage_const_0 
    for j in range(m):
        curr += sample_basis[i][j] * ciph[block_id][j]
    R_right.append(curr)

R_right_adj = []

R_mat_arr = []
for i in range(n-a):
    curr = []
    for j in range(n):
        curr.append(R[i].monomial_coefficient(xs[j]))
    R_right_adj.append(R_right[i] + FF(-R[i].constant_coefficient()))
    R_mat_arr.append(curr)


FUCKME = _sage_const_12 

R_mat = Matrix(FF, R_mat_arr)
soln = R_mat.augment(vector(R_right_adj)).echelon_form()
R_sice = PolynomialRing(FF, ["sice{}".format(i) for i in range(FUCKME)])
sices = R_sice.gens()
print(soln)

eqns = []

for i in range(n-FUCKME):
    curr = _sage_const_0 
    for j in range(FUCKME):
        curr += soln[i][j+n-FUCKME] * sices[j]
    curr = soln[i][n] - curr
    eqns.append(curr)

for j in range(FUCKME):
    eqns.append(sices[j])

poly_subs = {}
for i in range(n):
    poly_subs[xs[i]] = eqns[i]
new_poly = [pk[i].subs(poly_subs) for i in range(m)]

# ptxt_block = make_blocks(flag)[1]
# print ptxt_block
# print repr(combine_blocks([ptxt_block]))
# import ipdb
# ipdb.set_trace()

ctr = _sage_const_0 
for trial in FF**FUCKME:
    if ctr % _sage_const_1000  == _sage_const_0 :
        print(ctr)
    ctr += _sage_const_1 
    corr = True
    for i in range(m):
        if new_poly[i](*trial) != ciph[block_id][i]:
            corr = False
            break
    if corr:
        ans = [eqns[i](*trial) for i in range(n)]
        print(ans)
        break
