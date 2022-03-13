#coding a message, maybe to your girl friend:)

dic = {"a":0, "b":1,"c":2,"ç":3,"d":4,"e":5,"f":6,"g":7,"ğ":8,"h":9,"ı":10,"i":11,"j":12,"k":13,"l":14,"m":15,"n":16,"o":17,"ö":18,"p":19,"r":20,"s":21,"ş":22,"t":23,"u":24,"ü":25,"v":26,"y":27,"z":28," ":29,"?":30}
h = input("Şifrelenmesini istediğiniz cümleyi yazınız")
deneme = []
for m in h:
  deneme.append(dic[m])
print(deneme)


#if you don't want to write all these letters, try this!

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
print(çevrim)

#or

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {}
for i in harfler :
    cevrim[i]=harfler.index(i)
print(cevrim)
