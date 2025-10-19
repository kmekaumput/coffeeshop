from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template with embedded CSS and images
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dark Roast Coffee House</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #1a0f0a 0%, #2d1810 50%, #1a0f0a 100%);
            color: #d4a574;
            min-height: 100vh;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            padding: 60px 20px;
            background: rgba(0, 0, 0, 0.3);
            border-bottom: 2px solid #8b6f47;
            margin-bottom: 40px;
            position: relative;
            overflow: hidden;
        }

        header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&q=80') center/cover;
            opacity: 0.15;
            z-index: -1;
        }

        h1 {
            font-size: 3.5em;
            color: #d4a574;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
            margin-bottom: 10px;
            letter-spacing: 2px;
        }

        .subtitle {
            font-size: 1.2em;
            color: #b89968;
            font-style: italic;
        }

        .nav {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin: 30px 0;
            flex-wrap: wrap;
        }

        .nav a {
            color: #d4a574;
            text-decoration: none;
            padding: 10px 25px;
            background: rgba(139, 111, 71, 0.2);
            border: 1px solid #8b6f47;
            border-radius: 5px;
            transition: all 0.3s ease;
        }

        .nav a:hover {
            background: rgba(139, 111, 71, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(212, 165, 116, 0.3);
        }

        .hero {
            text-align: center;
            padding: 120px 20px;
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                        url('https://images.unsplash.com/photo-1511920170033-f8396924c348?w=1200&q=80') center/cover;
            border-radius: 10px;
            margin-bottom: 60px;
            position: relative;
        }

        .hero h2 {
            font-size: 2.5em;
            color: #f4e4c1;
            margin-bottom: 20px;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.8);
        }

        .hero p {
            font-size: 1.2em;
            color: #d4a574;
            max-width: 600px;
            margin: 0 auto;
            text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.8);
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 60px 0;
        }

        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            height: 250px;
            border: 2px solid #8b6f47;
            transition: all 0.3s ease;
        }

        .gallery-item:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(212, 165, 116, 0.3);
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        .gallery-item:hover img {
            transform: scale(1.1);
        }

        .gallery-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
            padding: 20px;
            transform: translateY(100%);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover .gallery-overlay {
            transform: translateY(0);
        }

        .gallery-overlay h4 {
            color: #f4e4c1;
            margin-bottom: 5px;
        }

        .gallery-overlay p {
            color: #d4a574;
            font-size: 0.9em;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }

        .card {
            background: rgba(45, 24, 16, 0.6);
            border: 1px solid #8b6f47;
            border-radius: 10px;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(212, 165, 116, 0.2);
            background: rgba(45, 24, 16, 0.8);
        }

        .card-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .card-content {
            padding: 30px;
        }

        .card h3 {
            color: #f4e4c1;
            margin-bottom: 15px;
            font-size: 1.8em;
        }

        .card p {
            color: #d4a574;
            margin-bottom: 10px;
        }

        .price {
            font-size: 1.5em;
            color: #8b6f47;
            font-weight: bold;
            margin-top: 15px;
        }

        .feature-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin: 60px 0;
            align-items: center;
        }

        .feature-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 10px;
            border: 2px solid #8b6f47;
        }

        .feature-text h2 {
            color: #f4e4c1;
            margin-bottom: 20px;
            font-size: 2.5em;
        }

        .feature-text p {
            color: #d4a574;
            font-size: 1.1em;
            margin-bottom: 15px;
        }

        footer {
            text-align: center;
            padding: 40px 20px;
            margin-top: 60px;
            border-top: 2px solid #8b6f47;
            color: #b89968;
        }

        .coffee-icon {
            font-size: 3em;
            margin: 20px 0;
        }

        @media (max-width: 768px) {
            h1 {
                font-size: 2.5em;
            }
            
            .hero h2 {
                font-size: 2em;
            }

            .feature-section {
                grid-template-columns: 1fr;
            }

            .gallery {
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="coffee-icon">☕</div>
        <h1>Dark Roast Coffee House</h1>
        <p class="subtitle">Where Every Cup Tells a Story</p>
    </header>

    <div class="container">
        <nav class="nav">
            <a href="/">Home</a>
            <a href="/menu">Menu</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>

        <section class="hero">
            <h2>Experience the Perfect Brew</h2>
            <p>Handcrafted coffee from the finest beans, roasted to perfection in our artisan roastery.</p>
        </section>

        <!-- Image Gallery Section -->
        <h2 style="text-align: center; color: #f4e4c1; margin-bottom: 30px;">Our Craft</h2>
        <div class="gallery">
            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1610632380989-680fe40816c6?w=600&q=80" alt="Professional Espresso Machine">
                <div class="gallery-overlay">
                    <h4>Professional Equipment</h4>
                    <p>State-of-the-art espresso machines</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&q=80" alt="Coffee Beans">
                <div class="gallery-overlay">
                    <h4>Premium Beans</h4>
                    <p>Sourced from the finest regions</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1511920170033-f8396924c348?w=600&q=80" alt="Latte Art">
                <div class="gallery-overlay">
                    <h4>Latte Art</h4>
                    <p>Crafted by skilled baristas</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=600&q=80" alt="Coffee Roasting">
                <div class="gallery-overlay">
                    <h4>Artisan Roasting</h4>
                    <p>Roasted fresh daily in-house</p>
                </div>
            </div>
        </div>

        <!-- Feature Section with Image -->
        <div class="feature-section">
            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800&q=80" alt="Coffee Bar" class="feature-image">
            <div class="feature-text">
                <h2>Our Coffee Bar</h2>
                <p>Step into our cozy coffee bar where passion meets perfection. Every cup is carefully crafted using our top-of-the-line espresso machines and premium beans.</p>
                <p>Our expert baristas bring years of experience and dedication to every pour, ensuring that each visit is a memorable coffee experience.</p>
            </div>
        </div>

        <h2 style="text-align: center; color: #f4e4c1; margin: 60px 0 30px;">Our Signature Blends</h2>
        
        <div class="card-grid">
            <div class="card">
                <img src="https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=600&q=80" alt="Espresso" class="card-image">
                <div class="card-content">
                    <h3>Midnight Espresso</h3>
                    <p>Rich, bold, and intense. Our darkest roast with notes of dark chocolate and caramel.</p>
                    <p><strong>Origin:</strong> Colombian Supremo</p>
                    <div class="price">$4.50</div>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1561047029-3000c68339ca?w=600&q=80" alt="Latte" class="card-image">
                <div class="card-content">
                    <h3>Velvet Latte</h3>
                    <p>Smooth and creamy with a perfect balance of espresso and steamed milk.</p>
                    <p><strong>Origin:</strong> Ethiopian Yirgacheffe</p>
                    <div class="price">$5.25</div>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=600&q=80" alt="Cappuccino" class="card-image">
                <div class="card-content">
                    <h3>Shadow Cappuccino</h3>
                    <p>Classic Italian style with a thick, velvety foam and robust espresso base.</p>
                    <p><strong>Origin:</strong> Brazilian Santos</p>
                    <div class="price">$4.75</div>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1485808191679-5f86510681a2?w=600&q=80" alt="Mocha" class="card-image">
                <div class="card-content">
                    <h3>Dark Mocha</h3>
                    <p>Decadent blend of dark chocolate and our signature espresso.</p>
                    <p><strong>Origin:</strong> Guatemalan Antigua</p>
                    <div class="price">$5.50</div>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?w=600&q=80" alt="Cold Brew" class="card-image">
                <div class="card-content">
                    <h3>Cold Brew Reserve</h3>
                    <p>Smooth, naturally sweet cold brew steeped for 18 hours.</p>
                    <p><strong>Origin:</strong> Sumatran Mandheling</p>
                    <div class="price">$5.00</div>
                </div>
            </div>

            <div class="card">
                <img src="https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&q=80" alt="Affogato" class="card-image">
                <div class="card-content">
                    <h3>Affogato Noir</h3>
                    <p>Vanilla gelato drowned in a double shot of hot espresso.</p>
                    <p><strong>Origin:</strong> Italian Blend</p>
                    <div class="price">$6.00</div>
                </div>
            </div>
        </div>

        <!-- Another Feature Section -->
        <div class="feature-section" style="margin-top: 80px;">
            <div class="feature-text">
                <h2>Latte Art Mastery</h2>
                <p>Our baristas are trained in the delicate art of latte decoration. Each cup is not just a beverage, but a canvas for creativity.</p>
                <p>From classic rosettas to intricate tulips, we pour our heart into every design, making your coffee experience truly Instagram-worthy.</p>
            </div>
            <img src="https://images.unsplash.com/photo-1511920170033-f8396924c348?w=800&q=80" alt="Latte Art" class="feature-image">
        </div>
    </div>

    <footer>
        <div class="coffee-icon">☕</div>
        <p>&copy; 2025 Dark Roast Coffee House. All rights reserved.</p>
        <p>Open Daily: 6:00 AM - 10:00 PM</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

@app.route('/menu')
def menu():
    return render_template_string(template.replace(
        'Our Signature Blends',
        'Full Menu - Coming Soon'
    ))

@app.route('/about')
def about():
    return render_template_string(template.replace(
        'Experience the Perfect Brew',
        'About Our Coffee House'
    ).replace(
        'Handcrafted coffee from the finest beans, roasted to perfection in our artisan roastery.',
        'Founded in 2020, we are passionate about bringing you the finest coffee experience.'
    ))

@app.route('/contact')
def contact():
    return render_template_string(template.replace(
        'Experience the Perfect Brew',
        'Get In Touch'
    ).replace(
        'Handcrafted coffee from the finest beans, roasted to perfection in our artisan roastery.',
        'Visit us at 123 Coffee Lane or email us at hello@darkroast.com'
    ))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)