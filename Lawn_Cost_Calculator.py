# Yash Sharma
# Python application for a lawn service provider
# This project is for a lawn service provider to calculate the cost while providing the serive by entering the area of lawn manually

# WELCOME_NOTE
print("------Hello! Welcome to the LAWN SETUP COST CALCULATOR------")
print("Kindly provide the necessary details to proceed futher")

# Getting Details of the LAWN
print("-------------------------------------------------------")
print("Enter the details of your FRONT YARD LAWN")
print("Enter the Width (in ft) = ")
front_yard_width=int(input())
print("Enter the Depth (in ft) = ")
front_yard_depth=int(input())
print("-------------------------------------------------------")
print("Enter the details of your REAR YARD LAWN")
print("Enter the Width (in ft) = ")
rear_yard_width=int(input())
print("Enter the Depth (in ft) = ")
rear_yard_depth=int(input())
print("-------------------------------------------------------")



#Calculating Area of Front Yard Lawn
print("-------------------------------------------------------")
print("------------------AREA of YOUR LAWN--------------------")
print("-------------------------------------------------------")

#Calculating Area of Front Yard Lawn
area_front=front_yard_depth*front_yard_width
print("Area Of FRONT YARD LAWN (in sq. ft) = ",area_front)

#Calculating Area of Rear Yard Lawn
area_rear=rear_yard_depth*rear_yard_width
print("Area Of FRONT YARD LAWN (in sq. ft) = ",area_rear)

#Calculating Total Area
total_area=area_rear+area_front
print("Total Area Of the Lawn (Area of Front + REAR YARD LAWN)",total_area, "sq.ft")



#Calculating the Cost of application of Fertilization
print("-------------------------------------------------------")
print("----------Cost of Application of Fertilizer------------")
print("-------------------------------------------------------")

#Cost of Application
print("Cost of application of fertilation in 1 sq.ft = ")
cost=int(input)

#Cost of single application
single_cost=(total_area)*cost
print("Cost of Single application of fertilizer $",single_cost)

#Cost of Full season application
season_cost= (4 * single_cost) -  (0.1 * 4 * single_cost)
print("Cost of Full Season application of fertilizer (10% Discount) $",season_cost)
print("------------------------------------------")
print("--------------THANK YOU-------------------")
