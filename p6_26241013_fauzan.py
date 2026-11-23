nama = "fauzan azima"
nim = "26241013"
A = 1
B = 3

print("nama :",nama)
print("nim :",nim)

a = int(input("Digit A:"))
b = int(input("Digit B:"))

kondisi1 = a >= 5
kondisi2 = b >= 5

print("kondisi 1 >= 5 :", kondisi1)
print("kondisi 2 >= 5 :", kondisi2)

print("NOT :",not kondisi1)
print("AND :",kondisi1 and kondisi2)
print("OR :",kondisi1 or kondisi2)
print("XOR :",kondisi1 ^ kondisi2)


#menggapa di logika xor,minsalnya true xor true =false ,sedangkan di and  ,hasilnya =true?
#dan mengapa di logika or dan xor,minsalnya false or dan xor true =true ,sedangkan di and ,hasilnya =flase?