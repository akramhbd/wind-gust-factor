import math

B = 30
L = 50
h = 120
V = 65.7
# ---------------------------------------------
epsilon = 0.333
alpha = 0.25
b = 0.45
z_min = 9.14
c = 0.3
g_Q = 3.4
l = 97.54
n1 = 0.25
beta = 0.02
g_v = 3.4

z = max(0.6*h, z_min)
I_z = c*(10/z)**(1/6)

print("z =", z)
print("I_z =", I_z)
L_z = (l*(z/10)**epsilon)
print("L_z =", L_z)
Q = math.sqrt(1/(1+0.63*((B+h)/L_z)**0.63))
print("Q =", Q)
print("n1 =", n1)
g_R = math.sqrt(2*math.log(3600*n1))+(0.577/(math.sqrt(2*math.log(3600*n1))))
print("g_R =", g_R)
V_z = b*((z/10)**alpha)*V
print("V_z =", V_z)
N1 = (n1*L_z)/V_z
print("N1 =", N1)
R_n = (7.47*N1)/((1+10.3*N1)**(5/3))
print("R_n =", R_n)

eta_h = 4.6*n1*(h/V_z)
eta_B = 4.6*n1*(B/V_z)
eta_L = 15.4*n1*(L/V_z)

R_h = (1/eta_h)-(1/(2*eta_h**2))*(1-math.exp(-2*eta_h))
R_B = (1/eta_B)-(1/(2*eta_B**2))*(1-math.exp(-2*eta_B))
R_L = (1/eta_L)-(1/(2*eta_L**2))*(1-math.exp(-2*eta_L))

R = math.sqrt((1/beta)*R_n*R_h*R_B*(0.53+0.47*R_L))

print("eta_h, eta_B, eta_L =", eta_h, eta_B, eta_L)
print("R_h, R_B, R_L =", R_h, R_B, R_L)
print("R =", R)

temp1 = (g_Q*Q)**2
temp2 = (g_R*R)**2
temp3 = math.sqrt(temp1+temp2)
temp4 = (1+1.7*I_z*temp3)/(1+1.7*g_v*I_z)

G_f = 0.925*temp4

print("G_f =", G_f)

