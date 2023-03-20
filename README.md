## MNIST dataseti yordamida qo'lda yozilgan raqamlarni bashorat qilish

#### 1. ```MNIST``` dataseti haqida qisqacha ma'lumot
```MNIST``` (Modified National Institute of Standards and Technology) ma'lumotlar bazasi turli xil tasvirlarni qayta ishlash tizimlarini o'qitish uchun keng qo'llaniladigan qo'lda yozilgan raqamlarning katta ma'lumotlar bazasidir. Ma'lumotlar bazasi mashinani o'rganish sohasida o'qitish va sinovdan o'tkazish uchun ham keng qo'llaniladi. Ijodkorlar fikricha, NISTning oʻquv maʼlumotlar toʻplami - Amerika aholisini roʻyxatga olish byurosi xodimlaridan, sinov maʼlumotlar toʻplami esa amerikalik oʻrta maktab oʻquvchilaridan olingani uchun u mashinani oʻrganish boʻyicha tajribalar uchun unchalik mos emas edi. Oq-qora tasvirlar 28x28 pikselli matritsalarga joylashtirish uchun normallashtirilgan va kulrang kanal holatida shakllantirilgan.

```MNIST``` ma'lumotlar bazasida 60 000 ta o'quv tasvir(```train data```)lari va 10 000 ta sinov tasvir(```test data```)lari mavjud. 

![cmd](https://github.com/MisterFoziljon/MNIST/blob/main/rasmlar/digits.jpg)


#### 2. Loyihani yuklab olish uchun quyidagi ketma-ketlikni bajaring:
  * `windows+R` klavishlarini bosing va paydo bo'lgan oynaga `cmd` buyrug'ini yozing OK tugmachasini bosing.
  
  ![cmd](https://github.com/MisterFoziljon/MNIST/blob/main/rasmlar/cmd.png)

  * Loyihani quyidagi link yordamida yuklab oling. (Loyiha uchun yaratilgan fayl adresni o'zingiz ko'rsatishingiz mumkin)

        C:\> git clone https://github.com/MisterFoziljon/MNIST.git

  * Loyiha joylashgan faylga kiring.
         
        C:\> cd MNIST


#### 2. Proyektni ishlatish uchun kerakli modullarni virtual environment yaratib o'rnatib oling.
* O'zingizdagi pip ni so'nggi versiyasiga yangilang.

        C:\MNIST> python -m pip install --upgrade pip
        
* virtual environment yaratish uchun virtualenv modulini o'rnating.
        
        C:\MNIST> python -m pip install --user virtualenv

* Yangi environment yaratish uchun unga nom bering.
        
        C:\MNIST> python -m venv sizning_env
        
* Virtual environmentni ishga tushiring(aktivlashtiring).
        
        C:\MNIST> sizning_env\Scripts\activate.bat
        
* Virtual environment ichiga loyiha ishlashi uchun kerakli bo'lgan modullarni o'rnating (requirements.txt faylining ichida barchasi mavjud).
        
        (sizning_env) C:\MNIST> pip install -r requirements.txt
