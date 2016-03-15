
# coding: utf-8

# # INTRODUCTION
#     This project is related to designing a junk-yard magnet, which is an electromagnet type. Throughout this project, electromagnet operating principles and design techniques in terms of different load values and electromagnet types are covered. The electromagnet should be capable of lifting standard sized metal sheets and plates of Parker Steel Company.
#     Firstly, electromagnet operation, its types and some important losses are explained. Then, the design code, which is written in Pyhton language by using Ipython notebook with Anaconda, is explained in detailed.
# 

# ## Electromagnet
#     An electromagnet is a type of magnet in which the magnetic field is produced by an electric current. The magnetic field disappears when the current is turned off. The main advantage of an electromagnet over a permanent magnet is that the magnetic field can be rapidly manipulated over a wide range by controlling the amount of electric current. However, a continuous supply of electrical energy is required to maintain the field.
#     
# ![The Junkyard Electromagnet](http://s.hswstatic.com/gif/electromagnets-1.jpg)
#    
#     Electromagnets are widely used as components of other electrical devices, such as motors, generators, relays, loudspeakers, hard disks, MRI machines, scientific instruments, and magnetic separation equipment. Electomagnets are also employed in industry for picking up and moving heavy iron objects such as scrap iron and steel. A junk-yard electromagnet is shown in above.
#     
#     There lots of type of electromagnet for different industrial purposes. The common types of electromagnet is shown below(in Dropbox link). 
# ![Electromagnet Types](https://www.dropbox.com/s/v0peljkimo6f79x/electromagnet%20shapes.PNG?dl=0)
# 
#     My electromagnet design is applicable for any type of electromagnet, especially U-shaped. It has re-adjustable functions and variable areas, and also there are information steps for user friendly development. 
# 

# In[1]:

print "Welcome to the Electromagnet Design Code"


# In[2]:

print "B = Magnetic Field Density"
print "A = Cross Sectional Area"
print "uo = Permeability of Free Space" 
print "L = Pitch or Length of Former"

from math import pi, exp, sqrt
uo = float(4 * pi * 10**-7) 
print uo


# ## Calculation of the load
# 
#         The main goal of this design is to operate with the standard sized metal sheets and plates of Parker Steel Company. 
#     For this purpose, there are five types of material and an optional step, which is created for unlisted material. In order to 
#     calculate the weight of the load, the volume and corresponding density of the load are required. The length, width and the 
#     thickness of the load are requested and the corresponding density for the selected material is written automatically. The densities are obtained from http://www.psyclops.com/tools/technotes/materials/density.html.

# In[3]:

# CALCULATION OF LOAD FORCE in N 
print "Enter the diameters of the load"
print " For material type: \n For Stainless Steel Enter 1 \n For Carbon Steel Enter 2 \n For Aluminium Enter 3 \n For Titanium Enter 4 \n For Brass Enter 5" 
print " For unlisted material Enter 10"
material = float(raw_input("The load material: "))
if material == 1:
    ll = float(raw_input("Enter the length of the load in inches :"))
    ww = float(raw_input("Enter the width of the load in inches :"))
    tt = float(raw_input("Enter the thickness of the load in mm :"))
    llcm = ll * float(2.54)
    wwcm = ww * float(2.54)
    ttcm = tt / float(10)
    VV = float(llcm * wwcm * ttcm)
    density = float(7.81)
    mgg = VV * density
    mg = mgg / float(1000)
elif material == 2:
    ll = float(raw_input("Enter the length of the load in inches :"))
    ww = float(raw_input("Enter the width of the load in inches :"))
    tt = float(raw_input("Enter the thickness of the load in mm :"))
    llcm = ll * float(2.54)
    wwcm = ww * float(2.54)
    ttcm = tt / float(10)
    VV = float(llcm * wwcm * ttcm)
    density = float(7.83)
    mgg = VV * density
    mg = mgg / float(1000)
elif material == 3:
    ll = float(raw_input("Enter the length of the load in inches :"))
    ww = float(raw_input("Enter the width of the load in inches :"))
    tt = float(raw_input("Enter the thickness of the load in mm :"))
    llcm = ll * float(2.54)
    wwcm = ww * float(2.54)
    ttcm = tt / float(10)
    VV = float(llcm * wwcm * ttcm)
    density = float(2.7)
    mgg = VV * density
    mg = mgg / float(1000)
elif material == 4:
    ll = float(raw_input("Enter the length of the load in inches :"))
    ww = float(raw_input("Enter the width of the load in inches :"))
    tt = float(raw_input("Enter the thickness of the load in mm :"))
    llcm = ll * float(2.54)
    wwcm = ww * float(2.54)
    ttcm = tt / float(10)
    VV = float(llcm * wwcm * ttcm)
    density = float(4.51)
    mgg = VV * density
    mg = mgg / float(1000)
elif material == 5:
    ll = float(raw_input("Enter the length of the load in inches :"))
    ww = float(raw_input("Enter the width of the load in inches :"))
    tt = float(raw_input("Enter the thickness of the load in mm :"))
    llcm = ll * float(2.54)
    wwcm = ww * float(2.54)
    ttcm = tt / float(10)
    VV = float(llcm * wwcm * ttcm)
    density = float(8.70)
    mgg = VV * density
    mg = mgg / float(1000)
elif material == 10:
    ll = float(raw_input("Enter the length of the load in inches :"))
    ww = float(raw_input("Enter the width of the load in inches :"))
    tt = float(raw_input("Enter the thickness of the load in mm :"))
    llcm = ll * float(2.54)
    wwcm = ww * float(2.54)
    ttcm = tt / float(10)
    VV = float(llcm * wwcm * ttcm)
    density = float(raw_input("Enter the density of the material in g/cm^3 :"))
    mgg = VV * density
    mg = mgg / float(1000)
else:
    print " Wrong Entered Number, Please Enter again"
    
print "The weight of the load is %f in kg" %mg    
print "Fmg = The gravitational force produced by load "
Fmg = float(9.8 * mg)
print "Fmg is %f in N" %(Fmg)


#         In this step, calculation of magnetic force is covered. Magnetic flux density is limited around 1.5 T due to saturation. Cross sectional area of the core is calculated based on the weight of the load. And, to get better area parameters, there is an optional  re-adjusted area. Our design is based on circular area because of the stacking factor improvement and lower losses of the core.
# 
#     The force exerted by an electromagnet on a section of core material is:
# $$F = B^2A/2\mu_0$$
# 

# In[4]:

B = float(raw_input ("Enter an appropriate B value in T : ")) # Nominal 0.6 - 1.5 T 
A = Fmg * 2* uo / (B * B)
print "Cross Sectional Area (min) in m^2 : %f" %A
A = float(raw_input ("Enter Cross Sectional Area (A) in m^2 : ")) # TO GET BETTER APPROXIMATION OF AREA
dia_core = sqrt( A / pi )
dia_core = dia_core * float(1000)
print "For circular design ---> diameter of core : %f mm" %dia_core # CIRCULAR DESIGN

F = B * B * A / (2 * uo)
print "Force is %f in N and Fmg is %f in N" %(F,Fmg)

while True:
    if F < Fmg:
        print ("Not sufficient MMF, Enter new design values")
        A = float(raw_input("Enter Cross Sectional Area (A) in m^2 : "))
        F = B * B * A / (2 * uo)
    else:
        break


#     Throughout this part, 
#         Firstly, lifting distance is requested and pre_design core length (roughly) is requested. For unsufficient core length, code gives an error at the end. According to flux path in both core and air gap, MMF is calculated. After entering number of turns for given MMF value, current on the wire is obtained.
# ### Selection of the material
#     Solid steel is generally best, in terms of economics, for the yoke, or frame, of static field devices. The mass of material required to efficiently carry flux between the far poles of an assembly make anything else impossible to justify. The reluctance of this part of the magnetic circuit is relatively low, even without annealing, compared to that of the working gap, so the losses associated with driving flux through the material are a small portion of overall losses
#     
# ### Losses of Electromagnet by choosing current
#     The only power consumed in a DC electromagnet is due to the resistance of the windings, and is dissipated as heat.Since the MMF is proportional to the product NI,the number of turns in the windings N and the current I can be chosen to minimize heat losses, as long as their product is constant. Since the power dissipation, 
#     
#  $$P = I^2R$$
#      
#     ,increases with the square of the current but only increases approximately linearly with the number of windings, the power lost in the windings can be minimized by reducing I and increasing the number of turns N proportionally, or using thicker wire to reduce the resistance; However, the limit to increasing N or lowering the resistance is that the windings take up more room between the magnet’s core pieces. If the area available for the windings is filled up, more turns require going to a smaller diameter of wire, which has higher resistance, which cancels the advantage of using more turns.
#     

# ## Electromagnet Design Procedure (for U shaped)
#     U shaped electromagnet is shown below. It has two airgap and two wire turn area. The core is in a circular form.
#     
# ![U-shaped Electromagnet](http://www.sciencescope.us/images/1070720_3.jpg)
# 
#     Applying Ampere's Law to the circuit,
#     
# $$\sum_{}^\ i = 2Ni = \int_{S}^{} H dl = H_{s}l_{s} + 2H_{g}l_{g}$$
# 
#     where Hs is the value of H in the core path, which is assumed to be constant and ls is the total length of the core path. At the boundary the magnetic flux densities are equal.
# $$ B_{s} = B_{g}$$
# 
#     Actually, 
#     
# $$H_{s}l_{s} << 2H_{g}l_{g}$$
# 
#     However, nothing is neglected to get accurate result. Therefore,
#     
# $$F = 2Ni = \phi(R_{s} + 2R{g})$$
# 
#     where:
# $$R_{s} = l_{s}/\mu\mu_0A_{s}$$
# $$R_{g} = l_{g}/\mu_0A_{g}$$    
# 

# In[5]:

# CALCULATION OF CURRENT 

L_gap = float(raw_input("Enter the lifting distance in mm :")) # FOR CONTACTED LIFTING => L_gap = 0.1 mm

L_core = float(raw_input("Enter the length of the core in cm :")) # LATER, it will be CHECKED
L_core = L_core * 10
print "Length of the core is %f in mm" %L_core

L_path = 2 * L_core + 2 * L_gap
print "Path of Flux is %f in mm" %L_path

L_path = L_path / float(1000) #ADJUSTED THE LENGTHS in m 
L_core = L_core / float(1000)
L_gap = L_gap / float(1000)
print " L_core = %f / L_gap = %f  / L_path = %f in m" %(L_core, L_gap, L_path)

print " Permeability : For Iron (99.8% pure) is 6.3 * 10^-3 H/m"
print " Permeability : For Electrical steel is  5 * 10^-3 H/m"
print " Permeability : For Platinum is  1.256970 * 10^-6 H/m"
print " Permeability : For Aluminum is  1.256665 * 10^-6 H/m"
u = float(raw_input("Enter the selected material's permeability in H/m : "))

MMF = B * (L_core / u * uo  + 2 * L_gap / uo) # Multiple L_gap with how many air_gap of the design
print "MMF is %f (A/m)" %MMF

N = raw_input("Enter the total number of turns : ")

#offset = float(raw_input("Determine an offset for MMF : ")) #OPTINAL FOR SAFETY 
#I = (MMF + offset) / float(N)

I = MMF / float(N)
print " Required Current is %f (A)" %I


#     According to calculated current value, appropriate wire is selected in this step. The list is obtained from http://en.wikipedia.org/wiki/American_wire_gauge and http://www.powerstream.com/Wire_Size.htm
#     The sufficient selection of wire improves the performances by reducing the losses around the wire and core.
# 
# ### Attention !!
#     The excel table of the wire is not embedded in the code. Therefore, you have to change the line, which indicates the location of the excel file.
#     The excel file can be downloaded from https://www.dropbox.com/s/e46f0idnv303z25/Copper_wires.xlsx?dl=0.
#     

# In[6]:

# SELECTION OF WİRE TYPE FROM COPPER WIRES
import xlrd
file_location = "C:\Users\ASUS\Desktop\Copper_wires.xlsx"
workbook = xlrd.open_workbook(file_location, "rb")
sheet = workbook.sheet_by_index(0)
#print sheet.nrows
#print sheet.ncols

for row in range(sheet.nrows):
    if I > sheet.cell_value(row,4):
        print "AWG gauge for the wire is %d " %sheet.cell_value(row-1,0)
        diameter_wire = sheet.cell_value(row-1,1)
        print "Diameter of selected wire is %f mm" %sheet.cell_value(row-1,1)
        resistance_wire = sheet.cell_value(row-1,2)/ float(1000)
        print "Resistances per m of selected wire is %f ohm/m" %resistance_wire
        break


#     At the last part, all calculations is operated by considering both one layer of wire turns and multiple layer.Multiple
#     layer is needed when the core length is not enough to contain all the wire turns. 
#     Then,
#         Total resistance of wire, flux, weight of the wire and required voltage are calculated, respectively.
#         
#     Total length of wire is calculated as:
# $$ T = L_{former} * stacking factor/d$$
#     where:
#           - T is the maximum number of turns in the first layer
#           - L_former is the length of core which the wire is wrapped. It should be smaller than length of the core.
#           - d = diamater of the selected wire.
# $$ n = N / T$$
#     where:
#           - n is the total number of layers
#           - N is the total number of turns
# $$ firstlayerlength = \pi D T$$
#     where:
#           - D is the diameter of the core
# $$Sum_{lengthofwire} = (n/2) (2 \pi D + (n-1)d)$$
# $$Total_Sum = Sum_{lengthofwire} * T $$
# 
#     The total resistance of the wire is calculated by using the AWG table.
# $$ R_{total} = Total_Sum * R_{ohm / m}$$
# 
#     The inductance of the coil is obtained as:
# $$ L = N \phi / I$$
#     where:
#           - L is the total inductance of the coil
#           - I is the current on the wire
#       
#     The total weight of the wire is calculated by using the diameter and density of the selected material. Material is mostly selected copper, which has the density 8.96 g/cm^3.
# $$ Volume_{wire} = \pi * (d/2)^2 * Total_sum$$
# $$ Weight_{wire} = Volume_{wire} * density_{material}$$
# 
#     The required voltage is obtained as:
# $$ V_{required} = I * R_{total}$$

# In[7]:

stacking = float(raw_input ("Enter the stacking factor : %f")) #roughly 0.9

# dia_meter is obtained
# dia_wire is obtained
# turn number is obtained
print "The entered length of the core is %f m" %L_core
L_former = float(raw_input("Enter the Length of Former in cm :"))
L_former = float (L_former * 10)
L_coremm = L_core * 1000 # Turn Lcore from m to mm

if L_former > L_coremm:
    print " L_former is longer than L_core, Please re-enter the L_core values"
    print "L_core value is %f" %L_core
    L_former = float(raw_input("Enter the Length of Former in cm :"))
    L_former = float (L_former * 10)



first = int (L_former * stacking / diameter_wire)
print " The maximum number of winding in the first layer is %f" %first

n = float(N) / first
n = int(n) + 1
print "the total number of layers required to give the total number of turns : %f" %n

Sum_length_wire = (float(n) / 2) * float(2 * pi * diameter_wire + (n-1) * diameter_wire)
Sum_length_wire = Sum_length_wire / float(10) # in cm

if N < first :
    Sum_length_wire = Sum_length_wire * float (N)
else:
    Sum_length_wire = Sum_length_wire * float (first)
    
print "Total Length of wire is %f (cm)" %Sum_length_wire

Sum_length_wire = Sum_length_wire / float(100) #in m
R_total = resistance_wire * Sum_length_wire 
print " The resistance of the wire is %f ohm " %R_total # TOO LOW VALUE OF RESISTANCES !!!!!!!!!


flux = float( B * A)
Inductance = float(N) * flux / I
print " The inductance of the coil is %f H" %Inductance


dia_wiree = diameter_wire / float(10)
dia_wire = dia_wiree / float(2)
density_copper = 8.96 # g / cm^-3

weight = pi* dia_wire * dia_wire * Sum_length_wire * density_copper
print " The weight of the wire is %f g" %weight


V_required = I * R_total
print " Required voltage for the electromagnet is %f V" %V_required










# # U-shaped Electromagnet Design Prodecure !!More Accurate!!
#     At this part is an optional area if the user is trying to design U-shaped electromagnet, far more accurately. It needs more       entries on core.
#     U-shaped electromagnet is shown below.
# ![U-shaped Electromagnet](http://ecx.images-amazon.com/images/I/41E4DEKHrcL.jpg)
# 
#     The user is used the obtained results and parameters, which are obtained above, to check more accurately.
#     All reluctances are included into the design below.
#     The magnetic circuit of the U-shaped electromagnet is shown below.
# 
# ![U-shaped Electromagnet Magnetic Circuit](https://www.dropbox.com/s/qbsdisp4p0arsv1/U-Shape%20Magnet.PNG?dl=0)
# 

#     Due to U-shape, there are two airgap.The force of attraction across each air gap between the electromagnet and total force is expressed, respectively. 
# $$M_{airgap} = NI/2$$
# $$R_{airgap} = g / \mu_0 A_{pole}$$
# 
# $$F_{magnet} = \mu_0 (NI)^2 A_{pole} / 4g^2$$
# 
#     where,
#            - M is the magneto-motive force across the each air gap 
#            - g is the length of the airgap
#            - R_airgap is the reluctance of the each airgap
#     Fmagnet equation shows that the magnetic force is a nonlinear function of both current and air gap length. And also, for a constant current the force decreases with increasing air gap, hence it has a negative stiffness coefficient. There is therefore no  point of equilibrium between two magnetised bodies and so the open-loop force-air gap characteristic of an electromagnet is unstable.
#     The assumption of uniform air gap flux distribution is valid only for air gaps that are much smaller than the pole width. At larger air gaps, flux fringing increases the effective air gap flux area and hence decreases the air gap reluctance.
#     
#     Directly lifting force is expressed below. For the loads in Parker Steel Company, the lateral offset (y) is zero.
# $$F_{lift} = F_{magnet}(1+(2g/\pi p)(1-(y/g)tan^-1(y/g)))$$
#     where,
#         - p is the pole width
#         - y is the lateral offset between the electromagnet and track poles. It is set to zero. 
#       
#     By considering zero lateral offset, 
# $$R_{airgap} = g / (\mu_0 l (p + 2g/\pi))$$
#     
#     Magnet and track path reluctance is calculated by summing the exact dimension entries. 
# $$R_{magnet} = (2h + w + 2p) / \mu_M \mu_0 lp$$
# $$R_{track} = (t + 4p)/ \mu_T \mu_0 lp$$
#     where,
#         - w is the width between the electromagnet poles
#         - p is the pole width
#         - h is the pole height above the yoke
#         - l is the length of the electromagnet
#         - t is the width between the track poles
#         - μM is the relavite permeability of electromagnet
#         - μT is the relavite permeability of track
#  
#     Leakage flux is calculated by neglecting fringe flux. Because air gap is so small for fringe flux calculation.
# $$R_{leakage} = w / \mu_0 l (h/2) $$
# 
#     All the parameters are obtained in the U-shaped magnetic circuit, shown above. After the analyzing the circuit, 
# $$ M_{airgap} = (R_{airgap}R_{leakage}/ (R_{track}+2R_{airgap})(R_{leakage}+R_{magnet}+R_{magnet}R_{leakage})) M_{coils}$$
#     where,
# $$M_{coils} = NI$$
# 
#     By substituting M_airgap into the function;
# $$F_{magnet} = M_{airgap}^2/g R_{airgap} $$
# 
# $$F_{magnet} = (R_{airgap}R_{leakage}^2/g((R_{track}+2R_{airgap})(R_{leakage}+R_{magnet}+R_{magnet}R_{leakage}))^2)M_{coils}^2$$
#     
#     F_lift is calculated by substituting F_magnet into F_lift function.
#     

# In[ ]:

print "Welcome to the Electromagnet Design Code"
print " U-SHAPE Electromagnet is covered in detailed "


# In[ ]:

while True:
    l = float(raw_input("Enter the length of Electromagnet in mm "))
    w = float(raw_input("Enter the Width between the electromagnet pole pieces in mm "))
    h = float(raw_input("Enter the Height of the pole pieces above the yoke in mm "))
    p = float(raw_input("Enter the Width of the pole pieces in mm "))
    if l >= (2 * h + w + 2 * p):
        print "The length of Electromagnet ERROR"
        print "l should be equal to (2 * h + w + 2 * p)"
        l = float(raw_input("Enter the length of Electromagnet in mm "))
        w = float(raw_input("Enter the Width between the electromagnet pole pieces in mm "))
        h = float(raw_input("Enter the Height of the pole pieces above the yoke in mm "))
        p = float(raw_input("Enter the Width of the pole pieces in mm "))
    else:
        break
    break
        
g = float(raw_input("Enter the length of Air gap in mm ")) # 0.1 mm for Contacted Lifting 
t = 0 # the width between the track poles


from math import pi, exp, sqrt, atan
uo = float(4 * pi * 10**-7) 
print " Permeability : For Iron (99.8% pure) is 6.3 * 10^-3 H/m"
print " Permeability : For Electrical steel is  5 * 10^-3 H/m"
print " Permeability : For Platinum is  1.256970 * 10^-6 H/m"
print " Permeability : For Aluminum is  1.256665 * 10^-6 H/m"
u = float(raw_input("Enter the selected material's permeability in H/m : "))


# In[ ]:

# RELUCTANCES
R_air = g / (uo * l * (p + 2 * g / pi)) #Air gap Reluctance
R_magnet = (2 * h + w + 2 * p) / (u * uo * l * p) # Core path Reluctance
R_leakage = w / (uo * l * h / 2) # Leakage Flux Reluctance *By neglecting fringing flux due to plate lifting*
R_track = (t + 4* p) / (u * uo * l * p)

print " R_air = %f" %R_air
print "R_magnet = %f" %R_magnet
print "R_leakage = %f" %R_leakage
print "R_track = %f" %R_track


# In[ ]:

N = raw_input("Enter the number of Turns : ")
I = raw_input("Enter the coil current in A : ")

M_coil = float(N) * float(I)
M_air = ((R_air * R_leakage) / ((R_track + 2 * R_air) * (R_leakage + R_magnet) + R_magnet * R_leakage)) * M_coil
print "M_air is %f" %M_air

F_magnet = M_air * M_air / (g * R_air)

y = 0 # Lateral offset
F_lift = F_magnet * (1 - ((y / g) * atan(y / g)) / (1 + pi * p / (2 * g) ))
print " Lifting Force is %f in N" %F_lift

# CALCULATION OF LOAD FORCE in N 

print "Fmg = The gravitational force produced by load "
mg = float(raw_input("Enter the weight of the load in kg : "))
Fmg = float(9.8 * mg)
print "Fmg is %f in N" %(Fmg)

if F_lift < Fmg:
    print "ERROR"
else:
    print "SUCCESSFUL DESIGN :)"
    


# #ADDITIONAL PART
# ## Determining the magnetic flux density at a distance X from the magnet at the center line, B(X)
#     For cylindrical shaped magnet, if the air gap is significantly high , this equation about B(x) is helpful to get better results.
#     The cylindrical shaped electromagnet and the dimensions are shown below,
# ![Cylindrical Shaped](https://www.dropbox.com/s/gw56hzvlqz57k8q/cylindrical%20shaped.PNG?dl=0)
# 
#     The equation is;
# $$B(x) = (B_r/2)((L + x)/\sqrt(R^2+(L+x)^2) - x/\sqrt(R^2+x^2))$$
#     where,
#         - Br is the residual flux density of the magnet
#         - x is the distance from the surface of the magnet
#         - L is the length of the magnet
#         - R is the radius of the magnet
# 
