"""Generates the privacy policy pages (Turkish + English) for Master Chicken games.

Usage: python3 -I build.py   → writes <app>.html and index.html next to this file.
"""
from pathlib import Path

UPDATED_TR = "22 Kasım 2026"
UPDATED_EN = "22 November 2026"
CONTACT = "gezer83serdar@gmail.com"

APPS = {
    "yonga": {"name": "Yonga", "package": "com.masterchicken.yonga", "accent": "#B4441F", "bg": "#FFF8EE", "share": True},
    "starhop": {"name": "Star Hop", "package": "com.masterchicken.starhop", "accent": "#9A6A00", "bg": "#FFFBEF", "share": False},
    "flipnir": {"name": "Flipnir", "package": "com.masterchicken.flipnir", "accent": "#A0127F", "bg": "#FFF6FC", "share": False},
    "huedrop": {"name": "Hue Drop", "package": "com.masterchicken.huedrop", "accent": "#2E7D12", "bg": "#F6FFF2", "share": False},
    "neonbridge": {"name": "Neon Bridge", "package": "com.masterchicken.neonbridge", "accent": "#00737F", "bg": "#F2FDFF", "share": False},
}


def tr(a):
    share = """
<h2>5. Sonuç paylaşma</h2>
<p>Günlük bulmacada “Sonucu paylaş” butonuna bastığınızda, puanınızı içeren kısa bir metin <strong>cihazınızda</strong> oluşturulur ve sizin seçtiğiniz uygulamaya (örneğin WhatsApp) aktarılır. Uygulama bu metni veya kiminle paylaştığınızı hiçbir yere göndermez ya da kaydetmez.</p>
""" if a["share"] else ""
    n = 6 if a["share"] else 5
    return f"""
<section lang="tr" id="tr">
<h1>{a['name']} – Gizlilik Politikası</h1>
<p class="date">Son güncelleme: {UPDATED_TR} · <a href="#en">English version below</a></p>

<p>Bu gizlilik politikası, Master Chicken tarafından yayınlanan <strong>{a['name']}</strong> oyununun (“Uygulama”, paket adı <code>{a['package']}</code>) hangi bilgileri nasıl işlediğini açıklar.</p>

<h2>1. Hesap ve kişisel bilgi</h2>
<p>Uygulama hesap oluşturmanızı istemez. Adınız, e-posta adresiniz, telefon numaranız, rehberiniz, fotoğraflarınız veya konumunuz gibi kişisel bilgileri <strong>toplamaz</strong>.</p>

<h2>2. Cihazda saklanan oyun verileri</h2>
<p>Skorlarınız, coinleriniz, açtığınız görünümler/bölümler ve ses-titreşim ayarlarınız yalnızca <strong>cihazınızda</strong> saklanır. Bu veriler bize veya başka bir sunucuya gönderilmez. Uygulamayı kaldırdığınızda silinir.</p>

<h2>3. Reklamlar (Google AdMob)</h2>
<p>Uygulama ücretsizdir ve Google AdMob aracılığıyla reklam gösterir (oyun arası reklamlar ve isteğe bağlı ödüllü videolar). AdMob, reklam göstermek, reklam performansını ölçmek ve sahtekârlığı önlemek amacıyla şu bilgileri toplayabilir:</p>
<ul>
  <li>Reklam kimliği (Android Advertising ID) ve cihaz bilgileri</li>
  <li>IP adresi ve buna dayalı yaklaşık konum</li>
  <li>Reklamlarla etkileşimler ve uygulama performansı/hata bilgileri</li>
</ul>
<p>Bu bilgiler Google tarafından işlenir. Ayrıntılar için: <a href="https://policies.google.com/technologies/partner-sites">Google, iş ortaklarının sitelerini veya uygulamalarını kullandığınızda verilerinizi nasıl kullanır</a> ve <a href="https://policies.google.com/privacy">Google Gizlilik Politikası</a>.</p>
<p><strong>Onay:</strong> Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre’deki kullanıcılardan, kişiselleştirilmiş reklamlar için Google’ın onay ekranı aracılığıyla izin istenir. Bu bölgelerde seçiminizi uygulamanın <em>Ayarlar → Gizlilik seçenekleri</em> bölümünden istediğiniz zaman değiştirebilirsiniz.</p>
<p><strong>Reklam kimliğinizi kontrol etmek:</strong> Android’de <em>Ayarlar → Google → Reklamlar</em> (veya <em>Ayarlar → Gizlilik → Reklamlar</em>) bölümünden reklam kimliğinizi sıfırlayabilir ya da silebilirsiniz.</p>

<h2>4. Uygulama içi satın alma</h2>
<p>“Reklamları kaldır” satın alımı Google Play faturalandırma sistemi üzerinden yapılır. Ödeme bilgileriniz Google tarafından işlenir; Uygulama bu bilgileri görmez. Uygulama yalnızca satın alımın tamamlandığı bilgisini alır ve bunu cihazınızda saklar.</p>
{share}
<h2>{n}. Çocuklar</h2>
<p>Uygulama 13 yaşından küçük çocuklara yönelik değildir ve bilerek çocuklardan kişisel veri toplamaz.</p>

<h2>{n + 1}. Veri güvenliği</h2>
<p>Uygulamanın kendisi sunucuda veri saklamaz. Google hizmetlerine (reklamlar, satın alma) giden bağlantılar şifreli (HTTPS) yapılır.</p>

<h2>{n + 2}. Değişiklikler</h2>
<p>Bu politika güncellenebilir. Güncel sürüm her zaman bu sayfada yayınlanır ve üstteki tarih değiştirilir.</p>

<h2>{n + 3}. İletişim</h2>
<p>Sorularınız için: <strong><a href="mailto:{CONTACT}">{CONTACT}</a></strong></p>
</section>
"""


def en(a):
    share = """
<h2>5. Sharing results</h2>
<p>When you tap “Share result” after the daily puzzle, a short text with your score is created <strong>on your device</strong> and handed to the app you choose (for example WhatsApp). The App does not send or store this text or who you share it with.</p>
""" if a["share"] else ""
    n = 6 if a["share"] else 5
    return f"""
<section lang="en" id="en">
<h1>{a['name']} – Privacy Policy</h1>
<p class="date">Last updated: {UPDATED_EN} · <a href="#tr">Türkçe sürüm yukarıda</a></p>

<p>This privacy policy explains what information the game <strong>{a['name']}</strong> (“the App”, package name <code>{a['package']}</code>), published by Master Chicken, handles and how.</p>

<h2>1. Accounts and personal information</h2>
<p>The App does not ask you to create an account. It does <strong>not</strong> collect personal information such as your name, email address, phone number, contacts, photos or location.</p>

<h2>2. Game data stored on your device</h2>
<p>Your scores, coins, unlocked skins/levels and sound and vibration settings are stored <strong>only on your device</strong>. They are not sent to us or to any server, and they are deleted when you uninstall the App.</p>

<h2>3. Ads (Google AdMob)</h2>
<p>The App is free and shows ads through Google AdMob (ads between games and optional reward videos). To show ads, measure ad performance and prevent fraud, AdMob may collect:</p>
<ul>
  <li>Advertising ID (Android Advertising ID) and device information</li>
  <li>IP address and approximate location derived from it</li>
  <li>Interactions with ads and app performance/crash information</li>
</ul>
<p>This information is processed by Google. See <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</p>
<p><strong>Consent:</strong> Users in the European Economic Area, the UK and Switzerland are asked for consent to personalised ads through Google’s consent form. In these regions you can change your choice at any time under <em>Settings → Privacy options</em> in the App.</p>
<p><strong>Controlling your advertising ID:</strong> On Android, go to <em>Settings → Google → Ads</em> (or <em>Settings → Privacy → Ads</em>) to reset or delete your advertising ID.</p>

<h2>4. In-app purchase</h2>
<p>The “Remove ads” purchase is made through Google Play Billing. Your payment details are processed by Google and are never visible to the App. The App only receives confirmation that the purchase was completed and stores that on your device.</p>
{share}
<h2>{n}. Children</h2>
<p>The App is not directed to children under 13 and does not knowingly collect personal data from children.</p>

<h2>{n + 1}. Data security</h2>
<p>The App itself does not store data on any server. Connections to Google services (ads, purchases) use encryption (HTTPS).</p>

<h2>{n + 2}. Changes</h2>
<p>This policy may be updated. The current version is always published on this page with the date above.</p>

<h2>{n + 3}. Contact</h2>
<p>Questions: <strong><a href="mailto:{CONTACT}">{CONTACT}</a></strong></p>
</section>
"""


def page(key, a):
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{a['name']} – Gizlilik Politikası / Privacy Policy</title>
<style>
  body{{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;max-width:720px;margin:0 auto;padding:32px 20px 64px;line-height:1.6;color:#16181D;background:{a['bg']}}}
  h1{{font-size:28px;margin-bottom:4px}}
  h2{{font-size:19px;margin-top:32px}}
  .date{{color:#5B6170;margin-top:0}}
  a{{color:{a['accent']}}}
  section + section{{margin-top:64px;padding-top:32px;border-top:2px solid #0001}}
  code{{font-size:.92em}}
</style>
</head>
<body>
{tr(a)}
{en(a)}
</body>
</html>
"""


root = Path(__file__).parent
for key, a in APPS.items():
    (root / f"{key}.html").write_text(page(key, a))
links = "\n".join(f'  <li><a href="{k}.html">{a["name"]}</a></li>' for k, a in APPS.items())
(root / "index.html").write_text(f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Master Chicken – Gizlilik / Privacy</title>
<style>body{{font-family:system-ui,sans-serif;max-width:640px;margin:0 auto;padding:32px 20px;line-height:1.6}}</style></head>
<body><h1>Master Chicken</h1><p>Gizlilik politikaları / Privacy policies</p><ul>
{links}
</ul></body></html>
""")
print("ok", sorted(p.name for p in root.glob("*.html")))
