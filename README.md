# وبلاگ حرفه‌ای دو زبانه با Django

یک وبلاگ کامل و حرفه‌ای با قابلیت‌های زیر:

## ویژگی‌ها

- **دو زبانه**: فارسی و انگلیسی با تغییر زبان آسان
- **تم روشن و تاریک**: با ذخیره در localStorage
- **ثبت‌نام کاربران**: ثبت‌نام، ورود، پروفایل با آواتار
- **پست‌ها با کاور**: امکان آپلود تصویر کاور و تصاویر داخل محتوا (CKEditor)
- **دسته‌بندی و تگ**: مدیریت کامل
- **نظرات**: با قابلیت پاسخ
- **جستجو**: جستجوی تمام‌متن در پست‌ها
- **پنل ادمین**: کامل با پشتیبانی ترجمه
- **طراحی واکنش‌گرا**: Bootstrap 5 + CSS سفارشی

## نصب و راه‌اندازی

```bash
# کلون یا استخراج zip
cd professional-blog

# ایجاد محیط مجازی (توصیه می‌شود)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# یا venv\Scripts\activate  # Windows

# نصب وابستگی‌ها
pip install -r requirements.txt

# مایگریشن
python manage.py makemigrations
python manage.py migrate

# ایجاد سوپریوزر
python manage.py createsuperuser

# جمع‌آوری فایل‌های استاتیک (اختیاری)
python manage.py collectstatic --noinput

# اجرای سرور
python manage.py runserver
```

سپس به آدرس http://127.0.0.1:8000 بروید.

## ساختار پروژه

```
├── config/          # تنظیمات اصلی
├── blog/            # اپ اصلی وبلاگ
│   ├── models.py    # Post, Category, Tag, Comment, Profile
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── accounts/        # احراز هویت
├── static/          # CSS و JS
├── templates/       # قالب پایه
├── media/           # فایل‌های آپلود شده
└── locale/          # ترجمه‌ها
```

## نکات مهم

1. برای ترجمه کامل، `msgfmt` را نصب کنید و `python manage.py compilemessages` بزنید.
2. در پروداکشن `DEBUG=False` و `SECRET_KEY` را تغییر دهید.
3. برای آپلود تصویر کاور، از پنل ادمین یا فرم ایجاد پست استفاده کنید.
4. مدل‌ها از modeltranslation برای فیلدهای دو زبانه پشتیبانی می‌کنند.

## لایسنس

MIT - آزاد برای استفاده شخصی و تجاری.
