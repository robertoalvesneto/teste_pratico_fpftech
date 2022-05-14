from vanitonpages.triangle import Triangle

if __name__ == "__main__":
    t = Triangle()

    website_url = "http://www.vanilton.net/triangulo/#"

    t.builder('firefox', website_url, [1, 2, 3])