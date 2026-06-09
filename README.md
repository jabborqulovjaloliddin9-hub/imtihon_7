# Blog API Tizimi (Blog API System)

Ushbu loyiha Django REST Framework (DRF) yordamida yaratilgan, Token Authentication tizimi bilan ishlovchi Blog API tizimidir. Tizimda foydalanuvchilar ro'yxatdan o'tishi, login/logout qilishi, postlar yaratishi, kommentlar yozishi hamda postlarga like bosishi mumkin.

## Texnologiyalar
- **Dasturlash tili:** Python
- **Freymvork:** Django, Django REST Framework
- **Autentifikatsiya:** Token Authentication
- **Ma'lumotlar bazasi:** SQLite (ishlab chiqish uchun)
- **Qo'shimcha:** django-filter (filtrlar uchun), Pillow (rasmlar uchun)

---

## O'rnatish va Ishga Tushirish Bosqichlari

### 1. Virtual Environment (Virtual Muhit) yaratish
Lokal muhitda loyihani mustaqil paketlar bilan ishga tushirish uchun virtual muhit yaratamiz:

```bash
# Windows uchun
python -m venv .venv
# Virtual muhitni faollashtirish (Windows)
.venv\Scripts\activate
```

### 2. Zarur kutubxonalarni o'rnatish
Loyiha ishlashi uchun zarur bo'lgan paketlarni `requirements.txt` yordamida o'rnatamiz:

```bash
pip install -r requirements.txt
```

### 3. `.env` faylini sozlash
Loyiha bosh papkasida `.env` nomli fayl yarating va unga quyidagi konfiguratsiyalarni yozing (hech qachon githubga yuklamang):

```env
SECRET_KEY=django-insecure-local-dev-key-12345
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 4. Ma'lumotlar bazasini yangilash (Migrations)
Modellar jadvalini yaratish va qo'llash:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser yaratish (Ixtiyoriy)
Admin panelga kirish va kategoriyalar yaratish uchun superuser ochish:

```bash
python manage.py createsuperuser
```

### 6. Loyihani ishga tushirish
Lokal serverni yoqamiz:

```bash
python manage.py runserver
```

---

## API Endpointlar Ro'yxati

### 1. Bosh sahifa (Welcome / Root)
* **Manzil:** `http://127.0.0.1:8000/` (GET) — API haqida umumiy ma'lumot va endpointlar ro'yxatini JSON shaklida qaytaradi.

### 2. Foydalanuvchilar va Autentifikatsiya (Auth)
| Tartib | Endpoint | Metod | Tavsif | Ruxsatnomalar (Permissions) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `/api/accounts/register/` | POST | Yangi foydalanuvchi ro'yxatdan o'tishi | Har kim (Anonymous) |
| 2 | `/api/accounts/login/` | POST | Tizimga kirish va Token olish | Har kim (Anonymous) |
| 3 | `/api/accounts/logout/` | POST | Tizimdan chiqish (Token o'chirish) | Login qilganlar (Authenticated) |
| 4 | `/api/accounts/profile/` | GET | Profil ma'lumotlarini ko'rish | Login qilganlar (Authenticated) |
| 5 | `/api/accounts/profile/` | PUT | Profil ma'lumotlarini qisman yangilash | Login qilganlar (Authenticated) |

### 3. Kategoriyalar (Categories)
| Tartib | Endpoint | Metod | Tavsif | Ruxsatnomalar (Permissions) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `/api/blog/categories/` | GET | Kategoriyalar ro'yxatini olish | Har kim |
| 2 | `/api/blog/categories/` | POST | Yangi kategoriya yaratish | Login qilganlar |

### 4. Postlar (Posts)
* **Qidiruv:** `/api/blog/posts/?search=post_sarlavhasi`
* **Filtrlash:** `/api/blog/posts/?category=kategoriya_id`
* **Tartiblash:** `/api/blog/posts/?ordering=-created_at` (yangi yaratilganlar birinchi)

| Tartib | Endpoint | Metod | Tavsif | Ruxsatnomalar (Permissions) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `/api/blog/posts/` | GET | Barcha postlarni ko'rish | Har kim |
| 2 | `/api/blog/posts/` | POST | Yangi post yaratish (rasm bilan) | Login qilganlar |
| 3 | `/api/blog/posts/<id>/` | GET | Postning batafsil ma'lumotlarini ko'rish | Har kim |
| 4 | `/api/blog/posts/<id>/` | PUT/PATCH | Postni o'zgartirish | Faqat post muallifi (Owner) |
| 5 | `/api/blog/posts/<id>/` | DELETE | Postni o'chirish | Faqat post muallifi (Owner) |

### 5. Kommentlar (Comments)
* **Filtrlash:** `/api/blog/comments/?post_id=post_id` (faqat shu postga tegishli kommentlar)

| Tartib | Endpoint | Metod | Tavsif | Ruxsatnomalar (Permissions) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `/api/blog/comments/` | GET | Barcha kommentlarni ko'rish | Har kim |
| 2 | `/api/blog/comments/` | POST | Yangi komment yozish | Login qilganlar |
| 3 | `/api/blog/comments/<id>/` | PUT/PATCH | Kommentni o'zgartirish | Faqat komment egasi (Owner) |
| 4 | `/api/blog/comments/<id>/` | DELETE | Kommentni o'chirish | Faqat komment egasi (Owner) |

### 6. Likelar (Likes)
| Tartib | Endpoint | Metod | Tavsif | Ruxsatnomalar (Permissions) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `/api/blog/posts/<post_id>/like/` | POST | Postga like bosish (faqat 1 marta) | Login qilganlar |
| 2 | `/api/blog/posts/<post_id>/like/` | DELETE | Likeni olib tashlash (Unlike) | Login qilganlar |
