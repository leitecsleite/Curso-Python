s1 = set()
s2 = set()

s1 = {1,2,3}
s2 = {2,4,3}

#União | União (union) = True
s3 = s1 | s2
print(s3)

#intersecção & - intens presentes em ambos

s3 = s1 & s2
print(s3)

#diferença - intens presentes apenas no set da esquerda 

s3 = s1 - s2
print(s3)

#diferença simétrica ^ - itens que não estão ambos
s3 = s1 ^ s2
print(s3)

