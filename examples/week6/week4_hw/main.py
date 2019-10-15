from geometry.area import square1,circle1,rectangle1,triangles1
from geometry.surface_area import cube2,cuboid2,cylinder2,sphere2
from geometry.volume import cube1,cuboid1,cylinder1,sphere1
print("两个以上数字输入，以英文逗号隔开")
a=eval(input("正方体的边长："))
x,y,z=eval(input("长方体的三边长："))
r=eval(input("圆的半径："))
l,R=eval(input("圆柱体的高和半径："))
c,d=eval(input("三角形底和高："))
print("正方体一个面的面积为{}，表面积为{}，体积为{}".format(square1.square2(a),cube2.cubes(a),cube1.cube(a)))
print("长方体一个面的面积为{}，表面积为{}，体积为{}".format(rectangle1.rectangle(x,y),cuboid2.cuboids(x,y,z),cuboid1.cuboid(x,y,z)))
print("一个圆的面积为{}，圆的表面积为{}，体积为{}".format(circle1.circle(r),sphere2.spheres(r),square1.square2(r)))
print("圆柱体的底面积为{}，表面积为{}，体积为{}".format(circle1.circle(R),cylinder2.cylinders(l,R),cylinder1.cylinder(l,R)))
print("三角形表面积为{}".format(triangles1.triangles(c,d)))