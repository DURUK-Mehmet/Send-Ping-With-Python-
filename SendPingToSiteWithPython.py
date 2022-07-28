import subprocess as sp 
#komutlar yazabilmemiz için subprecess kütüphanesini kullanıyoruz sp adlandırmasıyla

accept=[]
#pinglerin kabul edilen ve edilmeyen siteleri kaydetiğimiz accept ve rededilen denied listeleri
denied=[]

file=open("D:/Eğitimler/Python/IPAddress.txt","r")
#open kütüphanesi ile ıp adres'lerimizin bulunduğu konumu ve 
#   ne amaçla dosyayı kullanacağımzı(r,w,a,x) yazıyoruz ve bunlara erişmek için file nesnesini oluşturuyoruz 
ipAddress=file.read().split("\n")
#her okuduğu satırın sonunda bir alt satıra geçmek için \n ve düzenli olarak tutmak için ipAddress listesine atıyoruz
    
for ip in ipAddress:#ipAddress listesinideki elemanları tek tek ele almak için for döngüsü
    send_ping=sp.call("ping %s -n 4" % ip)
    #sp kütüüphanesinin call işlemine gönderilen ping komutumuz ve adresimiz
    #geri dönecek değer true veya false ise tutacak olan nesnemiz ise send_ping

    if send_ping==0:
        accept.append(ip)
        #send_ping eğer olumlu ise yani başarılı ping atılmış ise o adresi kabul edilenler listesine kaydediyoruz
    else:
        denied.append(ip)
        #send_ping eğer false ise yani başarısız ping atılmış ise o adresi kabul edilmeyenler listesine kaydediyoruz
        
file=open("D:/Eğitimler/Python/Accept.txt","w")
#open kütüphanesi ile kabul edilen ıp adres'lerimizi kaydedeceğimiz konumunu, dosya adı.uzantısını ve  
#   ne amaçla dosyayı kullanacağımzı(r,w,a,x) yazıyoruz ve bunlara erişmek için file nesnesini oluşturuyoruz 
for i in accept:
    file.write(i+"\n")
    #accept listesindeki elemanları alt alta gelecek şekilde oluşturulan Accept dosyasına kaydediyoruz
    
