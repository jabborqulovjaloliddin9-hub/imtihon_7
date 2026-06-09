from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.http import HttpResponse
from config import settings

def api_root(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="uz">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Blog API System</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-color: #0b0f19;
                --card-bg: #151b2c;
                --text-color: #f3f4f6;
                --text-muted: #9ca3af;
                --primary: #3b82f6;
                --primary-hover: #2563eb;
                --success: #10b981;
                --border-color: #1f2937;
            }
            body {
                font-family: 'Outfit', sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                max-width: 900px;
                width: 90%;
                margin: 60px auto;
            }
            header {
                text-align: center;
                margin-bottom: 40px;
            }
            h1 {
                font-size: 2.8rem;
                font-weight: 700;
                margin: 0 0 10px 0;
                background: linear-gradient(135deg, #60a5fa, #3b82f6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .subtitle {
                font-size: 1.1rem;
                color: var(--text-muted);
                margin-bottom: 20px;
            }
            .status-badge {
                display: inline-flex;
                align-items: center;
                background-color: rgba(16, 185, 129, 0.1);
                color: var(--success);
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 0.9rem;
                font-weight: 500;
                border: 1px solid rgba(16, 185, 129, 0.2);
            }
            .status-dot {
                width: 8px;
                height: 8px;
                background-color: var(--success);
                border-radius: 50%;
                margin-right: 8px;
                display: inline-block;
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0% { transform: scale(0.9); opacity: 0.6; }
                50% { transform: scale(1.2); opacity: 1; }
                100% { transform: scale(0.9); opacity: 0.6; }
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            .card {
                background-color: var(--card-bg);
                border: 1px solid var(--border-color);
                border-radius: 12px;
                padding: 24px;
                transition: transform 0.2s, border-color 0.2s;
            }
            .card:hover {
                transform: translateY(-4px);
                border-color: var(--primary);
            }
            .card h2 {
                font-size: 1.25rem;
                margin-top: 0;
                color: #ffffff;
                display: flex;
                align-items: center;
                gap: 8px;
            }
            .endpoint-list {
                list-style: none;
                padding: 0;
                margin: 15px 0 0 0;
            }
            .endpoint-item {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 8px 0;
                border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            }
            .endpoint-item:last-child {
                border-bottom: none;
            }
            .method {
                font-size: 0.75rem;
                font-weight: 700;
                padding: 2px 6px;
                border-radius: 4px;
                text-transform: uppercase;
            }
            .method.get { background-color: rgba(59, 130, 246, 0.15); color: #60a5fa; }
            .method.post { background-color: rgba(16, 185, 129, 0.15); color: #34d399; }
            .method.delete { background-color: rgba(239, 68, 68, 0.15); color: #f87171; }
            .method.put { background-color: rgba(245, 158, 11, 0.15); color: #fbbf24; }
            .path {
                font-family: monospace;
                font-size: 0.85rem;
                color: #93c5fd;
            }
            .footer {
                text-align: center;
                margin-top: 50px;
                color: var(--text-muted);
                font-size: 0.85rem;
            }
            a {
                color: var(--primary);
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Blog API System</h1>
                <div class="subtitle">Python & Django REST Framework yordamida yaratilgan mukammal API platformasi</div>
                <div class="status-badge">
                    <span class="status-dot"></span>
                    Tizim Statusi: Online
                </div>
            </header>
            
            <div class="grid">
                <!-- Auth Card -->
                <div class="card">
                    <h2>🔐 Autentifikatsiya (Auth)</h2>
                    <ul class="endpoint-list">
                        <li class="endpoint-item">
                            <span class="method post">POST</span>
                            <span class="path">/api/accounts/register/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method post">POST</span>
                            <span class="path">/api/accounts/login/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method post">POST</span>
                            <span class="path">/api/accounts/logout/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method get">GET</span>
                            <span class="path">/api/accounts/profile/</span>
                        </li>
                    </ul>
                </div>

                <!-- Blog Card -->
                <div class="card">
                    <h2>📝 Blog Postlar</h2>
                    <ul class="endpoint-list">
                        <li class="endpoint-item">
                            <span class="method get">GET</span>
                            <span class="path">/api/blog/posts/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method post">POST</span>
                            <span class="path">/api/blog/posts/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method get">GET</span>
                            <span class="path">/api/blog/posts/&lt;id&gt;/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method put">PUT</span>
                            <span class="path">/api/blog/posts/&lt;id&gt;/</span>
                        </li>
                    </ul>
                </div>

                <!-- Category, Comments & Likes Card -->
                <div class="card">
                    <h2>💬 Aloqadorliklar</h2>
                    <ul class="endpoint-list">
                        <li class="endpoint-item">
                            <span class="method get">GET</span>
                            <span class="path">/api/blog/categories/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method get">GET</span>
                            <span class="path">/api/blog/comments/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method post">POST</span>
                            <span class="path">/api/blog/posts/&lt;id&gt;/like/</span>
                        </li>
                        <li class="endpoint-item">
                            <span class="method delete">DEL</span>
                            <span class="path">/api/blog/posts/&lt;id&gt;/like/</span>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="footer">
                Loyihani boshqarish uchun <a href="/admin/" target="_blank">Admin Panel</a> ga kiring. Yaratuvchi: Antigravity IDE Agent
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)