buying_of_prod = {
    "piekarni": ["chleb", "bułki", "pączki"],
    "warzywniaka": ["marchew", "seler", "rukola"]
}

print("Lista zakupów", "\n")

for (shop, items) in buying_of_prod.items():
    items = ",".join(items)
    items = items.title()
    print(f"Idę do {shop.capitalize()}", "i kupuję tam:", items)

all_products = 0
for values in buying_of_prod.values():
    all_products += len(values)
print("W sumie kupuję:{} produktów".format(all_products))
