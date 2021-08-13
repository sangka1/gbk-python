from random import randint

ulang = 10
score_1 = 0
score_2 = 0

while ulang > 0:
  print("1. Gajah 2. Orang 3. Semut \n")
  pilih = int(input("pilih : "))
#Player 1 
  if pilih == 1:
     ulang -= 1
     print(f"Sisa Bermain : {ulang}")
     player_1 = "Gajah"
  elif pilih == 2:
     ulang -= 1
     print(f"Sisa Bermain : {ulang}")
     player_1 = "Orang"
  elif pilih == 3:
     ulang -= 1
     print(f"Sisa Bermain : {ulang}")
     player_1 = "Semut"
  else:
     print("Input salah ")

#player 2
  komputer = randint(1,3)
  if komputer == 1:
     player_2 = "Gajah"
  elif komputer == 2:
     player_2 = "Orang"
  elif komputer == 3:
     player_2 = "Semut"

#menentukan kemenangan
  if pilih == komputer:
     hasil = "Seri"
  elif pilih == 1 and komputer == 2:
     score_1 += 1
     hasil = "Anda Menang"
  elif pilih == 2 and komputer == 3:
     score_1 += 1
     hasil = "Anda Menang"
  elif pilih == 3 and komputer == 1:
     score_1 += 1
     hasil = "Anda Menang"
  elif komputer == 1 and pilih == 2:
     score_2 += 1
     hasil = "Anda Kalah"
  elif komputer == 2 and pilih == 3:
     score_2 += 1
     hasil = "Anda Kalah"
  elif komputer == 3 and pilih == 1:
     score_2 += 1
     hasil = "Anda Kalah"
     
  #menentukan hasil
  print(player_1)
  print(player_2)
  print(hasil)
  print("\n")
  
  if score_1 > score_2:
     print("anda menang, score anda adalah = ", score_1)
     print("sedangkan score musuh adalah = ", score_2)
  if score_1 < score_2:
     print("anda kalah score musuh adalah = ", score_2)
     print("sedangkan score anda adalah = ", score_1)
     
if ulang == 0:
   print("Game selesai")
