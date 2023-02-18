buying_of_prod = {
    "piekarni": ["chleb", "bułki", "pączki"],
    "warzywniaka": ["marchew", "seler", "rukola"],
}

print("Lista zakupów", "\n")
all_capitalize = []
all_products = 0
for (shop, items) in buying_of_prod.items():
    all_products += len(items)
    items = ",".join(items)
    print(f"Idę do {shop.capitalize()}", "i kupuję tam:", items.title())
print("W sumie kupuję: {} produktów".format(all_products))

print("Zgodnie z poleceniem przesyłam Ci Maciuś serdeczne pozdrowienia")
