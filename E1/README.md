
## ارتباط **سرور** و **کلاینت** با استفاده از سوکت‌ها

### 1. **کد سمت سرور**

این کد یک سرور ساده می‌سازه که درخواست‌های ارسالی از سمت کلاینت رو دریافت و بررسی می‌کنه. بعد از بررسی، پاسخ مناسب رو می‌فرسته.

#### مراحل اجرای کد سرور:

1. **ایجاد سوکت و پیکربندی آن:**

    ```python
    soc = socket.socket()
    soc.bind((ip, port))
    soc.listen(1)
    ```

در این قسمت، یک سوکت جدید ساخته می‌شه و به پورت 6969 متصل میشه. همچنین از دستور `listen(1)` استفاده می‌شه تا سرور فقط یک درخواست در هر لحظه رو قبول کنه.

2. **پذیرش اتصال از کلاینت:**

    ```python
    c, add = soc.accept()
    ```

در این بخش، سرور منتظر اتصال از سمت کلاینت می‌مونه و وقتی که کلاینت متصل شد، اتصال رو می‌پذیره.

3. **دریافت داده‌ها و ارسال پاسخ:**

    ```python
    data = c.recv(1024).decode()
    response = http_check(data)
    c.sendall(response)
    ```

پس از اتصال، داده‌های ارسالی از سمت کلاینت دریافت می‌شه و برای پردازش به تابع `http_check` ارسال می‌شه. در این تابع، درخواست بررسی می‌شه و نتیجه به‌عنوان پاسخ به کلاینت ارسال می‌شه.

4. **بستن اتصال:**

    ```python
    c.close()
    ```

در نهایت، اتصال پس از ارسال پاسخ بسته میشه.


#### بررسی درخواست HTTP:

در تابع `http_check`، سرور درخواست‌های مختلف HTTP رو بررسی می‌کنه:

- اگر متد درخواست `GET` نباشه، پاسخ 405 (Method Not Allowed) ارسال میشه.

- اگر مسیر درخواست `/moz.html` باشه، سرور فایل رو می‌خونه و محتوا رو به کلاینت می‌فرسته.

- در غیر این صورت، یک پاسخ 404 (Not Found) ارسال میشه.


### 2. **کد سمت کلاینت**

این کد وظیفه ارسال درخواست به سرور و دریافت پاسخ از آن را بر عهده داره. کلاینت از پروتکل HTTP برای درخواست دادن به سرور استفاده می‌کنه.

#### مراحل اجرای کد کلاینت:

1. **اتصال به سرور:**

    ```python
    client_socket.connect((addr, port))
    ```

ابتدا کلاینت به سرور (که در اینجا در لوکال‌هاست قرار داره) متصل میشه.

2. **ارسال درخواست HTTP:**

    ```python
    message = """GET /moz.html HTTP/1.1
    Host: 172.120.124.234:6969
    Connection: close\r\n\r\n
    """
    client_socket.send(message.encode())
    ```

در این مرحله، درخواست `GET` برای دریافت فایل `moz.html` به سرور ارسال میشه. توجه داشته باشید که درخواست به فرمت HTTP/1.1 ارسال میشه.

3. **دریافت و ذخیره پاسخ:**

    ```python
    data = client_socket.recv(1024).decode()
    save_html(data)
    ```

بعد از ارسال درخواست، پاسخ سرور دریافت و در تابع `save_html` ذخیره میشه.

4. **بستن اتصال:**

    ```python
    client_socket.close()
    ```

در نهایت پس از انجام تمام مراحل، اتصال به سرور بسته میشه.


#### ذخیره محتوا در فایل:

در تابع `save_html`، محتویات دریافت‌شده از سرور (که شامل HTML هست) در فایل `khiar.html` ذخیره میشه. این فایل در مسیر فعلی برنامه قرار می‌گیره.
