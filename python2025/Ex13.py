#There is a birthday celebration 
#Cake cutting 2 base , each base is 200 rs then went for the lunch with 10 peoples per plate rs 300 . Then in the dinner with 10 peoples and price is 400 rs.
#Find a total 20 peoples has given return gift with a money in cash 100 rs each. find the total , find the return gift total and investment in that event.
#list = cake cutting , lunch , dinner , return gift.

l1=[2,200,"cake"]
b=2
p=200
t=b*p
print(t)#total rs of cake

l2=[10,300,"lunch"]
p=10
r=300
l=p*r
print(l)#lunch 

l3=[10,400,"dinner"]
p=10
r=400
d=p*r
print(d)#Dinner

l4= [20,100,"returngift"]
p=20
r=100
t=p*r
print(t)#return gift

l5=[400,3000,4000,2000,"Balance"]
c=400
l=3000
d=4000
b=2000
t=c+l+d-b
print(t)#total balance