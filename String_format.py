#named indexs:
txt1 = "Welcome to {a:^15} {b:18}".format( a = "WsCube", b = "Tech")
#numbered indexes:
txt2 = "Welcome to {0:<13} {1} {2}". format("WsCube", "Tech", "shoaib")
#empty placeholders:
txt3 = "Welcome to {} {} {}".format("WsCube", "Tech", "shoaib")

print(txt1,type(txt1))
print(txt2,type(txt2))
print(txt3,type(txt3))