
# 📝 Django-Blog 

---

# 📝 وبلاگ حرفه‌ای دو زبانه با Django

![Django Version](https://img.shields.io/badge/Django-4.2+-092E20?style=flat&logo=django)
![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap)

یک وبلاگ کامل، مدرن و دو زبانه (فارسی/انگلیسی) با فریم‌ورک Django که تمام نیازهای یک وبلاگ حرفه‌ای را پوشش می‌دهد.

## ✨ ویژگی‌های برجسته

- 🌐 **دو زبانه (فارسی/انگلیسی)**: تغییر زبان با یک کلیک و پشتیبانی کامل از ترجمه
- 🌓 **تم روشن و تاریک**: ذخیره‌سازی خودکار در localStorage مرورگر
- 👤 **سیستم احراز هویت کامل**: ثبت‌نام، ورود، خروج، پروفایل کاربری با آواتار
- 🖼️ **مدیریت پیشرفته تصاویر**: آپلود تصویر کاور برای پست‌ها و استفاده از CKEditor برای محتوای غنی
- 🏷️ **دسته‌بندی و برچسب‌گذاری**: مدیریت کامل دسته‌بندی‌ها و تگ‌ها
- 💬 **سیستم نظرات**: با قابلیت پاسخ‌دهی به نظرات
- 🔍 **جستجوی تمام‌متن**: جستجوی پیشرفته در محتوای پست‌ها
- 🛠️ **پنل ادمین قدرتمند**: با پشتیبانی کامل از ترجمه و مدیریت آسان
- 📱 **طراحی واکنش‌گرا**: ساخته شده با Bootstrap 5 و CSS سفارشی

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 یا بالاتر
- pip
- virtualenv (توصیه می‌شود)

### مراحل نصب

1. **کلون کردن ریپازیتوری**
```bash
git clone https://github.com/GoldenIsland00/Django-Blog.git
cd Django-Blog
```

2. **ایجاد و فعال‌سازی محیط مجازی**
```bash
# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **نصب وابستگی‌ها**
```bash
pip install -r requirements.txt
```

4. **انجام مایگریشن‌ها**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **ایجاد کاربر ادمین**
```bash
python manage.py createsuperuser
```

6. **جمع‌آوری فایل‌های استاتیک (اختیاری)**
```bash
python manage.py collectstatic --noinput
```

7. **اجرای سرور توسعه**
```bash
python manage.py runserver
```

سپس به آدرس [http://127.0.0.1:8000](http://127.0.0.1:8000) مراجعه کنید.

## 📁 ساختار پروژه

```
├── config/              # تنظیمات اصلی پروژه
├── blog/                # اپ اصلی وبلاگ
│   ├── models.py        # مدل‌های Post, Category, Tag, Comment, Profile
│   ├── views.py         # ویوهای اصلی
│   ├── forms.py         # فرم‌های مورد استفاده
│   └── templates/       # قالب‌های مربوط به اپ blog
├── accounts/            # اپ مدیریت احراز هویت
├── static/              # فایل‌های استاتیک (CSS, JS, تصاویر)
├── templates/           # قالب‌های پایه پروژه
├── media/               # فایل‌های آپلود شده توسط کاربران
└── locale/              # فایل‌های ترجمه (فارسی/انگلیسی)
```

## ⚠️ نکات مهم

- برای فعال‌سازی کامل ترجمه، ابتدا `msgfmt` را نصب کرده و سپس دستور زیر را اجرا کنید:
  ```bash
  python manage.py compilemessages
  ```
- در محیط **پروداکشن** حتماً `DEBUG=False` را تنظیم کرده و `SECRET_KEY` را تغییر دهید.
- برای آپلود تصویر کاور، از پنل ادمین یا فرم ایجاد پست استفاده کنید.
- مدل‌ها از `django-modeltranslation` برای پشتیبانی از فیلدهای دو زبانه استفاده می‌کنند.

## 📞 ارتباط با من

- **ایمیل**: sirgae.youfski@gmail.com
- **گیت‌هاب**: [GoldenIsland00](https://github.com/GoldenIsland00)

