import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import re

try:
    import ttkbootstrap as tbs
    from ttkbootstrap.constants import *
except ImportError:
    import tkinter.ttk as tbs
    from tkinter.constants import *
    print("ttkbootstrap not found. Using default Tkinter styling.")

class SupermarketApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Market")
        self.root.geometry("1200x800")

        # Apply ttkbootstrap style with updated colors
        try:
            self.style = tbs.Style(theme="flatly")
            self.style.configure("TFrame", background="#F5F5DC")
            self.style.configure("TLabel", font=("Arial", 12), background="#F5F5DC")
            self.style.configure("TButton", font=("Arial", 10))
            self.style.configure("Header.TFrame", background="#D4EFDF")
            self.style.configure("Header.TLabel", font=("Arial", 20, "bold"), background="#D4EFDF", foreground="#1A3C5A")
            self.style.configure("Header.TButton", font=("Arial", 10, "bold"), padding=[8, 4], background="#D4EFDF", foreground="#000000")
            self.style.map("Header.TButton", background=[("active", "#28A745"), ("!active", "#D4EFDF")], foreground=[("active", "#FFFFFF")])
            self.style.configure("WhiteFrame.TFrame", background="#FDF5E6")
            self.style.configure("LightGrayFrame.TFrame", background="#F5F5DC")
            self.style.configure("WhiteCartFrame.TFrame", background="#FDF5E6")
            self.style.configure("OddRowFrame.TFrame", background="#FFE4E1")
            self.style.configure("ItemFrame.TFrame", background="#FDF5E6", relief="solid", borderwidth=1)
            self.style.configure("AddButton.TButton", background="#FF8C00", foreground="#FFFFFF", padding=3, font=("Arial", 10))
            self.style.map("AddButton.TButton", background=[("active", "#E07B00")])
        except:
            self.style = ttk.Style()
            self.style.configure("TFrame", background="#F5F5DC")
            self.style.configure("TLabel", background="#F5F5DC")
            self.style.configure("Header.TFrame", background="#D4EFDF")
            self.style.configure("Header.TLabel", font=("Arial", 20, "bold"), background="#D4EFDF", foreground="#1A3C5A")
            self.style.configure("Header.TButton", font=("Arial", 10, "bold"))
            self.style.configure("WhiteFrame.TFrame", background="#FDF5E6")
            self.style.configure("LightGrayFrame.TFrame", background="#F5F5DC")
            self.style.configure("WhiteCartFrame.TFrame", background="#FDF5E6")
            self.style.configure("OddRowFrame.TFrame", background="#FFE4E1")
            self.style.configure("ItemFrame.TFrame", background="#FDF5E6", relief="solid", borderwidth=1)
            self.style.configure("AddButton.TButton", background="#FF8C00", foreground="#FFFFFF")
            self.style.map("AddButton.TButton", background=[("active", "#E07B00")])

        # Data: Categories and Products (simplified for brevity)
        self.categories = [
            {
                "name": "Sports Nutrition",
                "items": [
                    {"id": 1, "name": "Clif Energy Bar", "description": "A high-energy snack with oats and chocolate chips, ideal for pre-workout fuel.", "price": 126 / 0.068, "unit": "kg"},
                    {"id": 2, "name": "Quest Protein Bar", "description": "High-protein bar with cookies and cream flavor, supports muscle recovery.", "price": 210 / 0.06, "unit": "kg"},
                    {"id": 3, "name": "Gatorade Sports Drink", "description": "Lemon-lime flavored drink to replenish electrolytes during intense workouts.", "price": 147 / 0.907, "unit": "kg"},
                    {"id": 4, "name": "Powerade", "description": "Mountain Berry Blast flavor, hydrates and boosts energy for athletes.", "price": 134.4 / 0.907, "unit": "kg"},
                    {"id": 5, "name": "Optimum Nutrition Whey Protein", "description": "Vanilla-flavored whey protein for muscle building and recovery.", "price": 2519.16 / 0.907, "unit": "kg"},
                    {"id": 6, "name": "Muscle Milk Protein Shake", "description": "Chocolate shake with high protein for post-workout nutrition.", "price": 252 / 0.397, "unit": "kg"},
                    {"id": 7, "name": "RXBAR Protein Bar", "description": "Peanut butter bar with natural ingredients for sustained energy.", "price": 189 / 0.052, "unit": "kg"},
                    {"id": 8, "name": "Nature Valley Protein Bar", "description": "Peanut butter and dark chocolate bar, great for on-the-go nutrition.", "price": 105 / 0.04, "unit": "kg"},
                    {"id": 9, "name": "Electrolyte Tablets", "description": "Nuun Sport tablets for hydration, packed with essential electrolytes.", "price": 587.16 / 0.05, "unit": "kg"},
                    {"id": 10, "name": "Gatorade Zero Powder", "description": "Fruit Punch flavored powder, zero sugar, for hydration.", "price": 503.16 / 0.05, "unit": "kg"},
                    {"id": 11, "name": "Kind Energy Bar", "description": "Dark chocolate nut bar, provides lasting energy for active lifestyles.", "price": 151.2 / 0.06, "unit": "kg"},
                    {"id": 12, "name": "Pure Protein Bar", "description": "Chocolate peanut butter bar, high protein for muscle support.", "price": 126 / 0.05, "unit": "kg"},
                    {"id": 13, "name": "BodyArmor Sports Drink", "description": "Tropical Punch flavor, packed with vitamins for superior hydration.", "price": 168 / 0.794, "unit": "kg"},
                    {"id": 14, "name": "Vega Protein Powder", "description": "Plant-based chocolate protein powder for vegan fitness enthusiasts.", "price": 2771.16 / 0.726, "unit": "kg"},
                    {"id": 15, "name": "Premier Protein Shake", "description": "Vanilla shake with 30g protein, low sugar, for post-workout recovery.", "price": 231 / 0.326, "unit": "kg"},
                    {"id": 201, "name": "MyProtein Impact Whey", "description": "Strawberry-flavored whey protein for muscle growth.", "price": 2399.16 / 0.900, "unit": "kg"},
                    {"id": 202, "name": "Skratch Labs Hydration Mix", "description": "Lemon-lime hydration mix for optimal electrolyte balance.", "price": 149.50 / 0.454, "unit": "kg"},
                    {"id": 203, "name": "Luna Protein Bar", "description": "Mint chocolate chip bar, high protein for recovery.", "price": 130 / 0.045, "unit": "kg"},
                    {"id": 204, "name": "Hammer Nutrition Gel", "description": "Apple-cinnamon gel for quick energy during workouts.", "price": 140 / 0.033, "unit": "kg"},
                    {"id": 205, "name": "BSN Syntha-6 Protein", "description": "Chocolate milkshake protein powder for post-workout.", "price": 2599.16 / 0.900, "unit": "kg"}
                ]
            },
            {
                "name": "Snacks",
                "items": [
                    {"id": 16, "name": "Lay’s Classic Potato Chips", "description": "Crispy potato chips with a classic salted flavor, perfect for snacking.", "price": 335.31, "unit": "pack"},
                    {"id": 17, "name": "Doritos Nacho Cheese", "description": "Bold nacho cheese-flavored tortilla chips, great for parties.", "price": 360.25, "unit": "pack"},
                    {"id": 18, "name": "Cheetos Crunchy", "description": "Crunchy cheese-flavored puffs, a fun and tasty snack.", "price": 318.12, "unit": "pack"},
                    {"id": 19, "name": "Pringles Original", "description": "Stackable potato chips with a unique original flavor.", "price": 209.03, "unit": "pack"},
                    {"id": 20, "name": "Tostitos Tortilla Chips", "description": "Corn tortilla chips, ideal for dipping with salsa or guacamole.", "price": 351.94, "unit": "pack"},
                    {"id": 21, "name": "Planters Mixed Nuts", "description": "A mix of peanuts, almonds, and cashews, lightly salted.", "price": 503.12, "unit": "pack"},
                    {"id": 22, "name": "Blue Diamond Almonds", "description": "Roasted and salted almonds, a healthy and crunchy snack.", "price": 628.79, "unit": "pack"},
                    {"id": 23, "name": "Sun-Maid Raisins", "description": "Sweet and chewy raisins, perfect for snacking or baking.", "price": 360.05, "unit": "pack"},
                    {"id": 24, "name": "Oreo Cookies", "description": "Classic chocolate sandwich cookies with creamy filling.", "price": 418.71, "unit": "pack"},
                    {"id": 25, "name": "Chips Ahoy! Cookies", "description": "Chocolate chip cookies, crispy and delicious.", "price": 326.78, "unit": "pack"},
                    {"id": 26, "name": "Goldfish Crackers", "description": "Cheddar-flavored fish-shaped crackers, fun for kids and adults.", "price": 234.12, "unit": "pack"},
                    {"id": 27, "name": "Ritz Crackers", "description": "Buttery, flaky crackers, great with cheese or spreads.", "price": 417.82, "unit": "pack"},
                    {"id": 28, "name": "Triscuit Crackers", "description": "Whole grain wheat crackers, perfect for healthy snacking.", "price": 293.06, "unit": "pack"},
                    {"id": 29, "name": "SkinnyPop Popcorn", "description": "Light and airy popcorn, low-calorie and gluten-free.", "price": 276.63, "unit": "pack"},
                    {"id": 30, "name": "Act II Microwave Popcorn", "description": "Butter-flavored popcorn for quick and easy movie nights.", "price": 377.04, "unit": "pack"},
                    {"id": 31, "name": "Rice Krispies Treats", "description": "Chewy marshmallow and rice cereal bars, a sweet treat.", "price": 267.87, "unit": "pack"},
                    {"id": 32, "name": "Nature Valley Granola Bars", "description": "Oats and honey granola bars, crunchy and wholesome.", "price": 360.00, "unit": "pack"},
                    {"id": 33, "name": "Chex Mix Traditional", "description": "Savory mix of cereal, pretzels, and nuts, perfect for snacking.", "price": 301.32, "unit": "pack"},
                    {"id": 34, "name": "Gardetto’s Snack Mix", "description": "Zesty mix of rye chips, pretzels, and seasonings.", "price": 309.88, "unit": "pack"},
                    {"id": 35, "name": "Pepperidge Farm Goldfish", "description": "Extra-large pack of cheddar Goldfish crackers, great for sharing.", "price": 838.95, "unit": "pack"},
                    {"id": 36, "name": "Hershey’s Milk Chocolate", "description": "Smooth milk chocolate bars, perfect for a sweet indulgence.", "price": 460.79, "unit": "pack"},
                    {"id": 37, "name": "Snickers Candy Bar", "description": "Peanuts, caramel, and chocolate in a satisfying candy bar.", "price": 108.44, "unit": "pack"},
                    {"id": 38, "name": "M&M’s Peanut", "description": "Peanut-filled chocolate candies, colorful and crunchy.", "price": 402.08, "unit": "pack"},
                    {"id": 39, "name": "Reese’s Peanut Butter Cups", "description": "Creamy peanut butter in milk chocolate cups, a classic treat.", "price": 443.54, "unit": "pack"},
                    {"id": 40, "name": "Twizzlers Licorice", "description": "Chewy strawberry-flavored licorice twists, fun to eat.", "price": 284.66, "unit": "pack"},
                    {"id": 41, "name": "Haribo Gummy Bears", "description": "Soft and fruity gummy bears, a favorite for all ages.", "price": 167.13, "unit": "pack"},
                    {"id": 42, "name": "True Elements Chia Seeds", "description": "Nutrient-rich chia seeds, great for smoothies and baking.", "price": 588.00, "unit": "pack"},
                    {"id": 43, "name": "Vedaka Whole Cashews", "description": "Premium whole cashews, perfect for snacking or cooking.", "price": 462.00, "unit": "pack"},
                    {"id": 44, "name": "Sunfeast Farmlite Biscuits", "description": "Healthy digestive biscuits, ideal with tea or coffee.", "price": 672.00, "unit": "pack"},
                    {"id": 45, "name": "Paper Boat Chikki Peanut Bar", "description": "Traditional peanut chikki, sweet and crunchy.", "price": 544.80, "unit": "pack"},
                    {"id": 46, "name": "Wonder Crème Confetti Cakes", "description": "Soft cakes with creamy filling and colorful sprinkles.", "price": 292.25, "unit": "pack"},
                    {"id": 47, "name": "Great Value Peanut Butter Pretzels", "description": "Pretzels filled with creamy peanut butter, a savory snack.", "price": 500.48, "unit": "pack"},
                    {"id": 48, "name": "Orion Rice Crackers", "description": "Light and crispy rice crackers, mildly flavored.", "price": 419.20, "unit": "pack"},
                    {"id": 49, "name": "Fruit Roll-Ups Variety Pack", "description": "Chewy fruit-flavored roll-ups, fun for kids.", "price": 359.97, "unit": "pack"},
                    {"id": 50, "name": "gimMe Seaweed Sheets", "description": "Roasted seaweed sheets with sea salt, a healthy snack.", "price": 504.00, "unit": "pack"},
                    {"id": 51, "name": "Kellogg’s Corn Pops", "description": "Sweet corn cereal, crunchy and kid-friendly.", "price": 418.71, "unit": "pack"},
                    {"id": 52, "name": "Nature’s Path Granola", "description": "Organic granola with nuts and seeds, perfect for yogurt.", "price": 502.74, "unit": "pack"},
                    {"id": 53, "name": "Pop Tarts (Strawberry)", "description": "Toasted pastries with strawberry filling, great for breakfast.", "price": 335.31, "unit": "pack"},
                    {"id": 54, "name": "Clif Shot Energy Gel", "description": "Quick-energy gel with mocha flavor, boosts performance.", "price": 151.20, "unit": "pack"},
                    {"id": 55, "name": "Sunchips Original", "description": "Whole grain chips with a mild, savory flavor.", "price": 293.06, "unit": "pack"}
                ]
            },
            {
                "name": "Fresh Produce",
                "items": [
                    {"id": 66, "name": "Apples (Gala)", "description": "Sweet and crisp Gala apples, perfect for snacking or baking.", "price": 246, "unit": "kg"},
                    {"id": 67, "name": "Bananas", "description": "Ripe yellow bananas, rich in potassium, great for smoothies.", "price": 109, "unit": "kg"},
                    {"id": 68, "name": "Oranges (Naval)", "description": "Juicy naval oranges, high in vitamin C, ideal for juicing.", "price": 265, "unit": "kg"},
                    {"id": 69, "name": "Strawberries", "description": "Fresh red strawberries, sweet and perfect for desserts.", "price": 647, "unit": "kg"},
                    {"id": 70, "name": "Blueberries", "description": "Antioxidant-rich blueberries, great for smoothies or yogurt.", "price": 987, "unit": "kg"},
                    {"id": 71, "name": "Grapes (Red Seedless)", "description": "Sweet and juicy red grapes, perfect for snacking.", "price": 555, "unit": "kg"},
                    {"id": 72, "name": "Watermelon (Mini)", "description": "Refreshing mini watermelon, ideal for summer picnics.", "price": 210, "unit": "kg"},
                    {"id": 73, "name": "Pineapple", "description": "Tropical pineapple, sweet and tangy, great for grilling.", "price": 184, "unit": "kg"},
                    {"id": 74, "name": "Avocados (Hass)", "description": "Creamy Hass avocados, perfect for guacamole or toast.", "price": 834, "unit": "kg"},
                    {"id": 75, "name": "Broccoli", "description": "Nutrient-packed broccoli, great for steaming or stir-frying.", "price": 425, "unit": "kg"},
                    {"id": 76, "name": "Carrots (Baby)", "description": "Sweet baby carrots, ideal for snacking or roasting.", "price": 332, "unit": "kg"},
                    {"id": 77, "name": "Tomatoes (Roma)", "description": "Firm Roma tomatoes, perfect for sauces and salads.", "price": 314, "unit": "kg"},
                    {"id": 78, "name": "Cucumbers", "description": "Crisp cucumbers, great for salads or pickling.", "price": 249, "unit": "kg"},
                    {"id": 79, "name": "Spinach", "description": "Fresh spinach leaves, rich in iron, ideal for smoothies.", "price": 739, "unit": "kg"},
                    {"id": 80, "name": "Lettuce (Iceberg)", "description": "Crisp iceberg lettuce, perfect for sandwiches and salads.", "price": 334, "unit": "kg"},
                    {"id": 81, "name": "Onions (Yellow)", "description": "Versatile yellow onions, essential for cooking and grilling.", "price": 185, "unit": "kg"},
                    {"id": 82, "name": "Potatoes (Russet)", "description": "Starchy russet potatoes, ideal for baking or mashing.", "price": 129, "unit": "kg"},
                    {"id": 83, "name": "Bell Peppers (Red)", "description": "Sweet red bell peppers, great for roasting or stuffing.", "price": 542, "unit": "kg"},
                    {"id": 84, "name": "Zucchini", "description": "Tender zucchini, perfect for grilling or baking.", "price": 332, "unit": "kg"},
                    {"id": 85, "name": "Mushrooms (White)", "description": "Fresh white mushrooms, ideal for soups and stir-fries.", "price": 811, "unit": "kg"},
                    {"id": 216, "name": "Kale", "description": "Nutrient-dense kale, perfect for salads or smoothies.", "price": 650, "unit": "kg"},
                    {"id": 217, "name": "Cauliflower", "description": "Versatile cauliflower, great for roasting or mashing.", "price": 420, "unit": "kg"},
                    {"id": 218, "name": "Bell Peppers (Yellow)", "description": "Sweet yellow bell peppers, ideal for salads or stir-fries.", "price": 550, "unit": "kg"},
                    {"id": 219, "name": "Mangoes", "description": "Juicy mangoes, perfect for smoothies or desserts.", "price": 780, "unit": "kg"},
                    {"id": 220, "name": "Kiwi", "description": "Tart and sweet kiwi, great for snacking or smoothies.", "price": 950, "unit": "kg"},
                    {"id": 221, "name": "Asparagus", "description": "Tender asparagus spears, ideal for grilling or steaming.", "price": 890, "unit": "kg"},
                    {"id": 222, "name": "Pears (Bartlett)", "description": "Sweet Bartlett pears, perfect for eating fresh or baking.", "price": 340, "unit": "kg"},
                    {"id": 223, "name": "Eggplant", "description": "Firm eggplant, great for grilling or making ratatouille.", "price": 310, "unit": "kg"}
                ]
            },
            {
                "name": "Dairy & Eggs",
                "items": [
                    {"id": 86, "name": "Whole Milk", "description": "Creamy whole milk, perfect for drinking or cooking.", "price": 84, "unit": "L"},
                    {"id": 87, "name": "2% Milk", "description": "Reduced-fat milk, great for cereal or coffee.", "price": 82, "unit": "L"},
                    {"id": 88, "name": "Almond Milk (Silk)", "description": "Plant-based almond milk, ideal for vegan diets.", "price": 155, "unit": "L"},
                    {"id": 89, "name": "Cheddar Cheese (Shredded)", "description": "Sharp cheddar cheese, perfect for melting or snacking.", "price": 1106, "unit": "kg"},
                    {"id": 90, "name": "Mozzarella Cheese (Shredded)", "description": "Soft mozzarella, ideal for pizzas and pastas.", "price": 1070, "unit": "kg"},
                    {"id": 91, "name": "Parmesan Cheese (Grated)", "description": "Aged Parmesan, great for grating over dishes.", "price": 1478, "unit": "kg"},
                    {"id": 92, "name": "Greek Yogurt (Chobani)", "description": "Thick Greek yogurt, high in protein, great for breakfast.", "price": 722, "unit": "kg"},
                    {"id": 93, "name": "Butter (Salted)", "description": "Rich salted butter, perfect for baking or spreading.", "price": 833, "unit": "kg"},
                    {"id": 94, "name": "Cream Cheese (Philadelphia)", "description": "Smooth cream cheese, ideal for bagels or dips.", "price": 1181, "unit": "kg"},
                    {"id": 95, "name": "Sour Cream", "description": "Creamy sour cream, great for tacos or baking.", "price": 425, "unit": "kg"},
                    {"id": 96, "name": "Large Eggs", "description": "Fresh large eggs, versatile for cooking and baking.", "price": 461, "unit": "kg"},
                    {"id": 97, "name": "Heavy Cream", "description": "Rich heavy cream, perfect for sauces or desserts.", "price": 620, "unit": "L"},
                    {"id": 98, "name": "Cottage Cheese", "description": "Creamy cottage cheese, great for snacks or salads.", "price": 517, "unit": "kg"},
                    {"id": 99, "name": "Yogurt (Yoplait)", "description": "Fruit-flavored yogurt, smooth and delicious.", "price": 440, "unit": "kg"},
                    {"id": 100, "name": "Half & Half", "description": "Blend of milk and cream, ideal for coffee or cooking.", "price": 266, "unit": "L"},
                    {"id": 224, "name": "Goat Cheese", "description": "Tangy goat cheese, perfect for salads or spreading.", "price": 1350, "unit": "kg"},
                    {"id": 225, "name": "Oat Milk (Oatly)", "description": "Creamy oat milk, great for coffee or cereal.", "price": 160, "unit": "L"},
                    {"id": 226, "name": "Feta Cheese", "description": "Crumbly feta, ideal for Mediterranean dishes.", "price": 1200, "unit": "kg"},
                    {"id": 227, "name": "Whipped Cream", "description": "Sweet whipped cream, perfect for desserts.", "price": 650, "unit": "L"},
                    {"id": 228, "name": "Soy Milk (Silk)", "description": "Smooth soy milk, a dairy-free alternative.", "price": 145, "unit": "L"}
                ]
            },
            {
                "name": "Meat & Seafood",
                "items": [
                    {"id": 101, "name": "Chicken Breast (Boneless)", "description": "Lean boneless chicken breast, perfect for grilling.", "price": 740, "unit": "kg"},
                    {"id": 102, "name": "Ground Beef (80/20)", "description": "80% lean ground beef, ideal for burgers or tacos.", "price": 925, "unit": "kg"},
                    {"id": 103, "name": "Pork Chops (Bone-In)", "description": "Juicy bone-in pork chops, great for baking or frying.", "price": 833, "unit": "kg"},
                    {"id": 104, "name": "Bacon", "description": "Smoky bacon strips, perfect for breakfast or burgers.", "price": 1111, "unit": "kg"},
                    {"id": 105, "name": "Sausage Links (Jimmy Dean)", "description": "Savory sausage links, great for breakfast or grilling.", "price": 1059, "unit": "kg"},
                    {"id": 106, "name": "Salmon Fillet (Fresh)", "description": "Fresh salmon fillet, rich in omega-3, ideal for baking.", "price": 1852, "unit": "kg"},
                    {"id": 107, "name": "Tilapia Fillet (Frozen)", "description": "Mild-flavored tilapia, perfect for quick meals.", "price": 1018, "unit": "kg"},
                    {"id": 108, "name": "Shrimp (Frozen, Raw)", "description": "Raw frozen shrimp, great for stir-fries or grilling.", "price": 1483, "unit": "kg"},
                    {"id": 109, "name": "Chicken Thighs (Boneless)", "description": "Tender boneless chicken thighs, ideal for curries.", "price": 647, "unit": "kg"},
                    {"id": 110, "name": "Ground Turkey", "description": "Lean ground turkey, a healthy alternative for meatballs.", "price": 795, "unit": "kg"},
                    {"id": 111, "name": "Beef Stew Meat", "description": "Cubed beef for hearty stews and slow-cooked dishes.", "price": 1203, "unit": "kg"},
                    {"id": 112, "name": "Hot Dogs (Ball Park)", "description": "Classic hot dogs, perfect for barbecues.", "price": 789, "unit": "kg"},
                    {"id": 113, "name": "Deli Ham (Sliced)", "description": "Thinly sliced ham, ideal for sandwiches or salads.", "price": 1295, "unit": "kg"},
                    {"id": 114, "name": "Deli Turkey (Sliced)", "description": "Sliced turkey breast, great for wraps or lunchboxes.", "price": 1388, "unit": "kg"},
                    {"id": 115, "name": "Tuna (Fresh)", "description": "Fresh tuna steak, perfect for grilling or sushi.", "price": 1667, "unit": "kg"},
                    {"id": 229, "name": "Cod Fillet (Fresh)", "description": "Mild white fish, great for baking or frying.", "price": 1450, "unit": "kg"},
                    {"id": 230, "name": "Pork Tenderloin", "description": "Lean pork tenderloin, perfect for roasting.", "price": 950, "unit": "kg"},
                    {"id": 231, "name": "Chicken Wings", "description": "Fresh chicken wings, ideal for frying or grilling.", "price": 680, "unit": "kg"},
                    {"id": 232, "name": "Lamb Chops", "description": "Tender lamb chops, great for grilling or pan-searing.", "price": 1800, "unit": "kg"},
                    {"id": 233, "name": "Crab Legs (Frozen)", "description": "Sweet crab legs, perfect for steaming.", "price": 2200, "unit": "kg"}
                ]
            },
            {
                "name": "Frozen Foods",
                "items": [
                    {"id": 116, "name": "Frozen Pizza (DiGiorno)", "description": "Pepperoni pizza with a rising crust, ready in minutes.", "price": 733, "unit": "kg"},
                    {"id": 117, "name": "Frozen Peas", "description": "Sweet green peas, perfect for soups or side dishes.", "price": 332, "unit": "kg"},
                    {"id": 118, "name": "Frozen Corn", "description": "Sweet corn kernels, ideal for stir-fries or grilling.", "price": 314, "unit": "kg"},
                    {"id": 119, "name": "Frozen Broccoli", "description": "Florets of broccoli, great for steaming or roasting.", "price": 492, "unit": "kg"},
                    {"id": 120, "name": "Frozen Strawberries", "description": "Sweet frozen strawberries, perfect for smoothies.", "price": 610, "unit": "kg"},
                    {"id": 121, "name": "Ice Cream (Ben & Jerry’s)", "description": "Chunky Monkey ice cream, rich and creamy dessert.", "price": 886, "unit": "L"},
                    {"id": 122, "name": "Frozen Chicken Nuggets (Tyson)", "description": "Crispy chicken nuggets, quick and easy for kids.", "price": 601, "unit": "kg"},
                    {"id": 123, "name": "Frozen French Fries (Ore-Ida)", "description": "Golden crinkle fries, perfect for baking or frying.", "price": 369, "unit": "kg"},
                    {"id": 124, "name": "Frozen Waffles (Eggo)", "description": "Homestyle waffles, great for quick breakfasts.", "price": 789, "unit": "kg"},
                    {"id": 125, "name": "Frozen Burritos (El Monterey)", "description": "Bean and cheese burritos, convenient for lunches.", "price": 525, "unit": "kg"},
                    {"id": 126, "name": "Frozen Fish Sticks (Gorton’s)", "description": "Crispy fish sticks, perfect for family dinners.", "price": 725, "unit": "kg"},
                    {"id": 127, "name": "Frozen Lasagna (Stouffer’s)", "description": "Classic meat lasagna, ready to bake for dinner.", "price": 987, "unit": "kg"},
                    {"id": 128, "name": "Frozen Blueberries", "description": "Sweet frozen blueberries, great for baking or smoothies.", "price": 740, "unit": "kg"},
                    {"id": 129, "name": "Frozen Spinach", "description": "Chopped spinach, ideal for dips or casseroles.", "price": 561, "unit": "kg"},
                    {"id": 130, "name": "Frozen Meatballs", "description": "Fully cooked meatballs, perfect for pasta or subs.", "price": 582, "unit": "kg"},
                    {"id": 234, "name": "Frozen Mixed Vegetables", "description": "Blend of carrots, peas, and corn, great for stir-fries.", "price": 350, "unit": "kg"},
                    {"id": 235, "name": "Ice Cream (Haagen-Dazs)", "description": "Vanilla ice cream, rich and creamy.", "price": 900, "unit": "L"},
                    {"id": 236, "name": "Frozen Mozzarella Sticks", "description": "Breaded mozzarella sticks, perfect for snacking.", "price": 620, "unit": "kg"},
                    {"id": 237, "name": "Frozen Tater Tots", "description": "Crispy tater tots, great as a side dish.", "price": 400, "unit": "kg"},
                    {"id": 238, "name": "Frozen Chicken Wings", "description": "Buffalo-style chicken wings, ready to heat and eat.", "price": 750, "unit": "kg"}
                ]
            },
            {
                "name": "Canned Goods",
                "items": [
                    {"id": 131, "name": "Canned Tuna (Chunk Light)", "description": "Chunk light tuna in water, great for salads or sandwiches.", "price": 108 / 0.142, "unit": "kg"},
                    {"id": 132, "name": "Canned Salmon", "description": "Wild-caught salmon, perfect for patties or spreads.", "price": 336 / 0.418, "unit": "kg"},
                    {"id": 133, "name": "Canned Black Beans", "description": "Pre-cooked black beans, ideal for soups or tacos.", "price": 83 / 0.425, "unit": "kg"},
                    {"id": 134, "name": "Canned Kidney Beans", "description": "Red kidney beans, great for chili or salads.", "price": 92 / 0.425, "unit": "kg"},
                    {"id": 135, "name": "Canned Corn", "description": "Sweet whole kernel corn, perfect for side dishes.", "price": 75 / 0.425, "unit": "kg"},
                    {"id": 136, "name": "Canned Green Beans", "description": "Tender green beans, ready for quick meals.", "price": 66 / 0.411, "unit": "kg"},
                    {"id": 137, "name": "Canned Tomato Sauce", "description": "Smooth tomato sauce, ideal for pasta or pizza.", "price": 58 / 0.425, "unit": "kg"},
                    {"id": 138, "name": "Canned Diced Tomatoes", "description": "Diced tomatoes, perfect for soups or sauces.", "price": 83 / 0.411, "unit": "kg"},
                    {"id": 139, "name": "Canned Tomato Paste", "description": "Concentrated tomato paste, great for cooking.", "price": 50 / 0.170, "unit": "kg"},
                    {"id": 140, "name": "Canned Chicken Noodle Soup", "description": "Hearty chicken noodle soup, ready to heat and eat.", "price": 125 / 0.297, "unit": "kg"},
                    {"id": 141, "name": "Canned Cream of Mushroom Soup", "description": "Creamy mushroom soup, ideal for casseroles.", "price": 117 / 0.297, "unit": "kg"},
                    {"id": 142, "name": "Canned Peaches", "description": "Sweet peaches in syrup, perfect for desserts.", "price": 142 / 0.425, "unit": "kg"},
                    {"id": 143, "name": "Canned Pineapple", "description": "Juicy pineapple chunks, great for baking or snacking.", "price": 150 / 0.567, "unit": "kg"},
                    {"id": 144, "name": "Canned Baked Beans", "description": "Savory baked beans in tomato sauce, a BBQ favorite.", "price": 108 / 0.453, "unit": "kg"},
                    {"id": 145, "name": "Canned Chili", "description": "Spicy beef chili, ready for a quick meal.", "price": 167 / 0.425, "unit": "kg"},
                    {"id": 239, "name": "Canned Chickpeas", "description": "Pre-cooked chickpeas, great for hummus or salads.", "price": 90 / 0.425, "unit": "kg"},
                    {"id": 240, "name": "Canned Cream of Chicken Soup", "description": "Creamy chicken soup, perfect for casseroles.", "price": 120 / 0.297, "unit": "kg"},
                    {"id": 241, "name": "Canned Mandarin Oranges", "description": "Sweet mandarin oranges in syrup, great for desserts.", "price": 130 / 0.425, "unit": "kg"},
                    {"id": 242, "name": "Canned Lentils", "description": "Pre-cooked lentils, ideal for soups or stews.", "price": 95 / 0.425, "unit": "kg"},
                    {"id": 243, "name": "Canned Mixed Vegetables", "description": "Blend of carrots, peas, and corn, ready to use.", "price": 80 / 0.425, "unit": "kg"}
                ]
            },
            {
                "name": "Grains & Pasta",
                "items": [
                    {"id": 146, "name": "White Rice (Long Grain)", "description": "Fluffy long-grain white rice, perfect for all dishes.", "price": 185, "unit": "kg"},
                    {"id": 147, "name": "Brown Rice", "description": "Nutritious brown rice, great for healthy meals.", "price": 277, "unit": "kg"},
                    {"id": 148, "name": "Spaghetti Pasta", "description": "Classic spaghetti, ideal for Italian dishes.", "price": 239, "unit": "kg"},
                    {"id": 149, "name": "Penne Pasta", "description": "Short tube pasta, perfect for hearty sauces.", "price": 258, "unit": "kg"},
                    {"id": 150, "name": "Macaroni", "description": "Elbow macaroni, great for mac and cheese.", "price": 221, "unit": "kg"},
                    {"id": 151, "name": "Quinoa", "description": "Protein-rich quinoa, ideal for salads or bowls.", "price": 833, "unit": "kg"},
                    {"id": 152, "name": "Oats (Old Fashioned)", "description": "Whole grain oats, perfect for breakfast or baking.", "price": 282, "unit": "kg"},
                    {"id": 153, "name": "Cheerios Cereal", "description": "Whole grain oat cereal, heart-healthy breakfast.", "price": 936, "unit": "kg"},
                    {"id": 154, "name": "Corn Flakes", "description": "Crispy corn flakes, a classic breakfast cereal.", "price": 575, "unit": "kg"},
                    {"id": 155, "name": "Raisin Bran", "description": "Bran flakes with sweet raisins, high in fiber.", "price": 695, "unit": "kg"},
                    {"id": 156, "name": "Couscous", "description": "Quick-cooking couscous, great for salads or sides.", "price": 680, "unit": "kg"},
                    {"id": 157, "name": "Instant Oatmeal", "description": "Flavored instant oatmeal, quick and nutritious.", "price": 739, "unit": "kg"},
                    {"id": 158, "name": "Farro", "description": "Nutty farro grain, perfect for soups or salads.", "price": 925, "unit": "kg"},
                    {"id": 159, "name": "Barley", "description": "Hearty barley, great for stews or risottos.", "price": 462, "unit": "kg"},
                    {"id": 160, "name": "Bulgur Wheat", "description": "Quick-cooking bulgur, ideal for tabbouleh.", "price": 610, "unit": "kg"},
                    {"id": 244, "name": "Wild Rice", "description": "Nutty wild rice, perfect for gourmet dishes.", "price": 950, "unit": "kg"},
                    {"id": 245, "name": "Lasagna Noodles", "description": "Wide pasta sheets, ideal for layered lasagna.", "price": 270, "unit": "kg"},
                    {"id": 246, "name": "Orzo Pasta", "description": "Small rice-shaped pasta, great for soups.", "price": 250, "unit": "kg"},
                    {"id": 247, "name": "Millet", "description": "Gluten-free millet, perfect for porridge or salads.", "price": 500, "unit": "kg"},
                    {"id": 248, "name": "Rice Noodles", "description": "Thin rice noodles, ideal for Asian dishes.", "price": 300, "unit": "kg"}
                ]
            },
            {
                "name": "Bakery",
                "items": [
                    {"id": 161, "name": "White Bread", "description": "Soft white bread, perfect for sandwiches or toast.", "price": 295, "unit": "kg"},
                    {"id": 162, "name": "Whole Wheat Bread", "description": "Nutritious whole wheat bread, great for health-conscious diets.", "price": 369, "unit": "kg"},
                    {"id": 163, "name": "Tortillas (Flour)", "description": "Soft flour tortillas, ideal for wraps or tacos.", "price": 480, "unit": "kg"},
                    {"id": 164, "name": "Bagels (Plain)", "description": "Chewy plain bagels, perfect for breakfast or lunch.", "price": 575, "unit": "kg"},
                    {"id": 165, "name": "English Muffins", "description": "Crisp English muffins, great for breakfast sandwiches.", "price": 689, "unit": "kg"},
                    {"id": 166, "name": "Hamburger Buns", "description": "Soft buns, perfect for burgers or sliders.", "price": 460, "unit": "kg"},
                    {"id": 167, "name": "Hot Dog Buns", "description": "Soft buns, ideal for hot dogs or sausages.", "price": 439, "unit": "kg"},
                    {"id": 168, "name": "Croissants", "description": "Buttery croissants, perfect for breakfast or snacks.", "price": 1676, "unit": "kg"},
                    {"id": 169, "name": "Muffins (Blueberry)", "description": "Moist blueberry muffins, great for on-the-go.", "price": 900, "unit": "kg"},
                    {"id": 170, "name": "Dinner Rolls", "description": "Soft dinner rolls, perfect for family meals.", "price": 627, "unit": "kg"},
                    {"id": 249, "name": "Sourdough Bread", "description": "Tangy sourdough loaf, great for sandwiches.", "price": 450, "unit": "kg"},
                    {"id": 250, "name": "Cinnamon Rolls", "description": "Sweet cinnamon rolls with icing, perfect for breakfast.", "price": 850, "unit": "kg"}
                ]
            },
            {
                "name": "Beverages",
                "items": [
                    {"id": 171, "name": "Coca-Cola", "description": "Classic carbonated cola, refreshing and crisp.", "price": 96, "unit": "L"},
                    {"id": 172, "name": "Pepsi", "description": "Bold and refreshing cola, perfect for meals.", "price": 118, "unit": "L"},
                    {"id": 173, "name": "Bottled Water", "description": "Pure purified water, ideal for hydration.", "price": 35, "unit": "L"},
                    {"id": 174, "name": "Orange Juice", "description": "Freshly squeezed orange juice, rich in vitamin C.", "price": 155, "unit": "L"},
                    {"id": 175, "name": "Apple Juice", "description": "Sweet apple juice, great for kids or cocktails.", "price": 146, "unit": "L"},
                    {"id": 176, "name": "Coffee (Ground, Folgers)", "description": "Medium roast ground coffee, perfect for brewing.", "price": 875, "unit": "kg"},
                    {"id": 177, "name": "Tea Bags (Lipton)", "description": "Black tea bags, ideal for hot or iced tea.", "price": 1886, "unit": "kg"},
                    {"id": 178, "name": "Sparkling Water (LaCroix)", "description": "Calorie-free sparkling water, crisp and refreshing.", "price": 104, "unit": "L"},
                    {"id": 179, "name": "Iced Tea (Lipton)", "description": "Sweetened iced tea, perfect for hot days.", "price": 89, "unit": "L"},
                    {"id": 180, "name": "Lemonade", "description": "Tangy lemonade, refreshing and sweet.", "price": 133, "unit": "L"},
                    {"id": 181, "name": "Kombucha (GT’s)", "description": "Probiotic-rich kombucha, supports gut health.", "price": 620, "unit": "L"},
                    {"id": 182, "name": "Coconut Water (Vita Coco)", "description": "Natural coconut water, hydrating and refreshing.", "price": 468, "unit": "L"},
                    {"id": 183, "name": "Green Tea (Arizona)", "description": "Lightly sweetened green tea, great for relaxation.", "price": 159, "unit": "L"},
                    {"id": 184, "name": "Hot Cocoa Mix (Swiss Miss)", "description": "Rich hot cocoa mix, perfect for cozy nights.", "price": 747, "unit": "kg"},
                    {"id": 185, "name": "Energy Drink (Red Bull)", "description": "Energizing drink with caffeine, boosts performance.", "price": 936, "unit": "L"},
                    {"id": 251, "name": "Sprite", "description": "Lemon-lime soda, crisp and refreshing.", "price": 100, "unit": "L"},
                    {"id": 252, "name": "Ginger Ale (Canada Dry)", "description": "Light ginger ale, great for sipping or mixing.", "price": 110, "unit": "L"},
                    {"id": 253, "name": "Cranberry Juice", "description": "Tart cranberry juice, rich in antioxidants.", "price": 170, "unit": "L"},
                    {"id": 254, "name": "Energy Drink (Monster)", "description": "High-caffeine energy drink for a quick boost.", "price": 950, "unit": "L"},
                    {"id": 255, "name": "Herbal Tea (Celestial)", "description": "Chamomile tea bags, perfect for relaxation.", "price": 1500, "unit": "kg"}
                ]
            },
            {
                "name": "Cooking Essentials",
                "items": [
                    {"id": 186, "name": "Olive Oil (Extra Virgin)", "description": "Premium extra virgin olive oil, ideal for cooking or dressings.", "price": 896, "unit": "L"},
                    {"id": 187, "name": "Canola Oil", "description": "Neutral-flavored canola oil, great for frying or baking.", "price": 295, "unit": "L"},
                    {"id": 188, "name": "Vegetable Oil", "description": "Versatile vegetable oil, perfect for all-purpose cooking.", "price": 266, "unit": "L"},
                    {"id": 189, "name": "All-Purpose Flour", "description": "Fine all-purpose flour, essential for baking and cooking.", "price": 111, "unit": "kg"},
                    {"id": 190, "name": "Granulated Sugar", "description": "Pure white sugar, ideal for baking or sweetening.", "price": 162, "unit": "kg"},
                    {"id": 191, "name": "Brown Sugar", "description": "Moist brown sugar, great for cookies or sauces.", "price": 212, "unit": "kg"},
                    {"id": 192, "name": "Baking Powder", "description": "Double-acting baking powder, essential for baking.", "price": 731, "unit": "kg"},
                    {"id": 193, "name": "Baking Soda", "description": "Pure baking soda, great for baking or cleaning.", "price": 239, "unit": "kg"},
                    {"id": 194, "name": "Vanilla Extract", "description": "Pure vanilla extract, adds rich flavor to desserts.", "price": 4266, "unit": "L"},
                    {"id": 195, "name": "Cocoa Powder", "description": "Unsweetened cocoa powder, perfect for chocolate desserts.", "price": 1291, "unit": "kg"},
                    {"id": 196, "name": "Salt (Table)", "description": "Fine table salt, essential for seasoning.", "price": 136, "unit": "kg"},
                    {"id": 197, "name": "Black Pepper (Ground)", "description": "Ground black pepper, adds spice to any dish.", "price": 2460, "unit": "kg"},
                    {"id": 198, "name": "Garlic Powder", "description": "Granulated garlic powder, perfect for seasoning.", "price": 2005, "unit": "kg"},
                    {"id": 199, "name": "Onion Powder", "description": "Fine onion powder, great for soups or rubs.", "price": 2490, "unit": "kg"},
                    {"id": 200, "name": "Paprika", "description": "Smoky paprika, adds color and flavor to dishes.", "price": 3360, "unit": "kg"},
                    {"id": 256, "name": "Coconut Oil", "description": "Pure coconut oil, ideal for cooking or baking.", "price": 920, "unit": "L"},
                    {"id": 257, "name": "Honey", "description": "Natural honey, perfect for sweetening or baking.", "price": 1100, "unit": "kg"},
                    {"id": 258, "name": "Cinnamon (Ground)", "description": "Warm ground cinnamon, great for baking or oatmeal.", "price": 2800, "unit": "kg"},
                    {"id": 259, "name": "Soy Sauce", "description": "Savory soy sauce, ideal for Asian dishes.", "price": 450, "unit": "L"},
                    {"id": 260, "name": "Chili Powder", "description": "Spicy chili powder, perfect for seasoning meats.", "price": 3100, "unit": "kg"}
                ]
            },
            {
                "name": "Cleaning Supplies",
                "items": [
                    {"id": 261, "name": "Dish Soap (Dawn)", "description": "Powerful dish soap, cuts through grease easily.", "price": 350, "unit": "L"},
                    {"id": 262, "name": "Laundry Detergent (Tide)", "description": "Effective detergent, removes tough stains.", "price": 800, "unit": "L"},
                    {"id": 263, "name": "All-Purpose Cleaner (Lysol)", "description": "Versatile cleaner, disinfects surfaces.", "price": 450, "unit": "L"},
                    {"id": 264, "name": "Glass Cleaner (Windex)", "description": "Streak-free glass cleaner, shines windows.", "price": 400, "unit": "L"},
                    {"id": 265, "name": "Sponges (Scotch-Brite)", "description": "Durable sponges, great for scrubbing dishes.", "price": 250, "unit": "pack"},
                    {"id": 266, "name": "Trash Bags (Glad)", "description": "Strong trash bags, prevents leaks.", "price": 600, "unit": "pack"},
                    {"id": 267, "name": "Bleach (Clorox)", "description": "Powerful bleach, disinfects and whitens.", "price": 500, "unit": "L"},
                    {"id": 268, "name": "Dishwasher Pods (Cascade)", "description": "Convenient pods, cleans dishes thoroughly.", "price": 700, "unit": "pack"},
                    {"id": 269, "name": "Fabric Softener (Downy)", "description": "Softens clothes, leaves a fresh scent.", "price": 650, "unit": "L"},
                    {"id": 270, "name": "Air Freshener (Febreze)", "description": "Odor-eliminating spray, fresh linen scent.", "price": 300, "unit": "pack"}
                ]
            },
            {
                "name": "Miscellaneous",
                "items": [
                    {"id": 271, "name": "AA Batteries (Energizer)", "description": "Long-lasting AA batteries, great for devices.", "price": 500, "unit": "pack"},
                    {"id": 272, "name": "Paper Towels (Bounty)", "description": "Absorbent paper towels, perfect for spills.", "price": 450, "unit": "pack"},
                    {"id": 273, "name": "Toilet Paper (Charmin)", "description": "Soft toilet paper, strong and absorbent.", "price": 600, "unit": "pack"},
                    {"id": 274, "name": "Aluminum Foil (Reynolds)", "description": "Durable foil, ideal for cooking or storage.", "price": 350, "unit": "pack"},
                    {"id": 275, "name": "Plastic Wrap (Saran)", "description": "Cling wrap, keeps food fresh.", "price": 300, "unit": "pack"},
                    {"id": 276, "name": "Ziploc Bags (Gallon)", "description": "Resealable bags, great for storage.", "price": 400, "unit": "pack"},
                    {"id": 277, "name": "Light Bulbs (Philips)", "description": "Energy-efficient LED bulbs, bright light.", "price": 550, "unit": "pack"},
                    {"id": 278, "name": "Duct Tape (3M)", "description": "Strong duct tape, versatile for repairs.", "price": 250, "unit": "pack"},
                    {"id": 279, "name": "Candles (Yankee)", "description": "Scented candles, vanilla aroma.", "price": 700, "unit": "pack"},
                    {"id": 280, "name": "Matches (Diamond)", "description": "Wooden matches, easy to light.", "price": 100, "unit": "pack"}
                ]
            }
        ]
   

        # Cart to store selected items
        self.cart = []

        # Hardcoded user data for the Account tab
        self.user_data = {
            "name": "John Doe",
            "email": "john.doe@example.com"
        }

        # Create main UI components
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.main_frame = ttk.Frame(self.root, style="LightGrayFrame.TFrame")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Header with title on the left and navigation buttons on the right
        self.header_frame = ttk.Frame(self.main_frame, style="Header.TFrame")
        self.header_frame.pack(fill="x", pady=(0, 10))

        # Title on the left
        title_frame = ttk.Frame(self.header_frame, style="Header.TFrame")
        title_frame.pack(side="left", padx=10)
        ttk.Label(title_frame, text="Super Market", style="Header.TLabel").pack(pady=10)

        # Navigation buttons on the right
        nav_frame = ttk.Frame(self.header_frame, style="Header.TFrame")
        nav_frame.pack(side="right", padx=10)

        self.products_button = ttk.Button(nav_frame, text="Products", style="Header.TButton", command=self.show_products)
        self.products_button.pack(side="right", padx=5)

        self.cart_button = ttk.Button(nav_frame, text="Cart", style="Header.TButton", command=self.show_cart)
        self.cart_button.pack(side="right", padx=5)

        self.account_button = ttk.Button(nav_frame, text="Account", style="Header.TButton", command=self.show_account)
        self.account_button.pack(side="right", padx=5)

        # Main content area
        self.content_frame = ttk.Frame(self.main_frame, style="WhiteFrame.TFrame")
        self.content_frame.pack(fill="both", expand=True)

        # Create all content frames
        self.products_main_frame = ttk.Frame(self.content_frame, style="WhiteFrame.TFrame")
        self.create_product_frame()

        self.cart_frame = ttk.Frame(self.content_frame, style="WhiteCartFrame.TFrame")
        self.create_cart_frame()

        self.account_frame = ttk.Frame(self.content_frame, style="WhiteFrame.TFrame")
        self.create_account_frame()

        self.payment_frame = ttk.Frame(self.content_frame, style="WhiteFrame.TFrame")
        self.create_payment_frame()

        # Initially show the Products frame
        self.current_frame = None
        self.show_products()

    def show_products(self):
        self.switch_frame(self.products_main_frame)

    def show_cart(self):
        self.switch_frame(self.cart_frame)

    def show_account(self):
        self.switch_frame(self.account_frame)

    def show_payment(self):
        self.switch_frame(self.payment_frame)

    def switch_frame(self, frame_to_show):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = frame_to_show
        self.current_frame.pack(fill="both", expand=True)

    def create_product_frame(self):
        # Category tabs notebook
        self.category_notebook = ttk.Notebook(self.products_main_frame)
        self.category_notebook.pack(fill="both", expand=True)

        # Create a tab for each category
        self.category_frames = {}
        for category in self.categories:
            category_name = category["name"]
            frame = ttk.Frame(self.category_notebook, style="WhiteFrame.TFrame")
            self.category_notebook.add(frame, text=category_name)
            self.category_frames[category_name] = frame
            self.update_products(category, frame)

    def update_products(self, category, parent_frame):
        # Products display with scrollbar
        canvas = tk.Canvas(parent_frame, bg="#FDF5E6")
        scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, style="WhiteFrame.TFrame")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.pack(side="right", fill="y")

        # Display items in a grid (4 items per row)
        items = category["items"]
        for row_idx in range((len(items) + 3) // 4):
            row_style = "OddRowFrame.TFrame" if row_idx % 2 == 0 else "WhiteFrame.TFrame"
            row_frame = ttk.Frame(scrollable_frame, style=row_style)
            row_frame.pack(fill="x", padx=2, pady=2)

            for col_idx in range(4):
                item_idx = row_idx * 4 + col_idx
                if item_idx >= len(items):
                    break
                item = items[item_idx]

                item_frame = ttk.Frame(row_frame, style="ItemFrame.TFrame", width=220, height=180)
                item_frame.pack(side="left", padx=2)
                item_frame.pack_propagate(False)

                short_desc = item["description"].split(", ")[1] if ", " in item["description"] else item["description"]

                ttk.Label(item_frame, text=item["name"], font=("Arial", 12, "bold"), wraplength=200).pack(anchor="w", padx=5, pady=2)
                ttk.Label(item_frame, text=f"{short_desc}, {item['unit']}", font=("Arial", 9), wraplength=200).pack(anchor="w", padx=5)
                price_label = ttk.Label(item_frame, text=f"${item['price']:.2f}", font=("Arial", 12), foreground="teal")
                price_label.pack(anchor="w", padx=5, pady=2)

                ttk.Button(
                    item_frame,
                    text="Add to Cart",
                    style="AddButton.TButton",
                    command=lambda i=item: self.add_to_cart(i, "1")
                ).pack(anchor="w", padx=5, pady=2)

    def add_to_cart(self, item, quantity):
        try:
            quantity = float(quantity)
            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be positive.")
                return
            self.cart.append({"item": item, "quantity": quantity})
            messagebox.showinfo("Success", f"{item['name']} added to cart!")
            self.update_cart()
        except ValueError:
            messagebox.showerror("Error", "Invalid quantity entered.")

    def create_cart_frame(self):
        # Cart header
        ttk.Label(self.cart_frame, text="Your Cart", font=("Arial", 16, "bold")).pack(pady=10)

        # Cart display
        self.cart_canvas = tk.Canvas(self.cart_frame, bg="#FDF5E6")
        self.cart_scrollbar = ttk.Scrollbar(self.cart_frame, orient="vertical", command=self.cart_canvas.yview)
        self.cart_scrollable_frame = ttk.Frame(self.cart_canvas, style="WhiteCartFrame.TFrame")

        self.cart_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.cart_canvas.configure(scrollregion=self.cart_canvas.bbox("all"))
        )

        self.cart_canvas.create_window((0, 0), window=self.cart_scrollable_frame, anchor="nw")
        self.cart_canvas.configure(yscrollcommand=self.cart_scrollbar.set)

        self.cart_canvas.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        self.cart_scrollbar.pack(side="right", fill="y")

        # Total label
        self.total_var = tk.StringVar(value="Total: $0.00")
        ttk.Label(self.cart_frame, textvariable=self.total_var, font=("Arial", 12, "bold")).pack(anchor="e", pady=10)

        # Payment options
        payment_frame = ttk.Frame(self.cart_frame, style="WhiteCartFrame.TFrame")
        payment_frame.pack(fill="x", pady=10)

        ttk.Button(payment_frame, text="Pay Now", command=self.handle_pay_now).pack(side="left", padx=20)
        ttk.Button(payment_frame, text="Pay on Delivery", command=self.handle_pay_on_delivery).pack(side="left", padx=20)

    def update_cart(self):
        # Clear current cart
        for widget in self.cart_scrollable_frame.winfo_children():
            widget.destroy()

        total = 0
        for idx, cart_item in enumerate(self.cart):
            item = cart_item["item"]
            quantity = cart_item["quantity"]
            item_total = item["price"] * quantity
            total += item_total

            item_frame = ttk.Frame(self.cart_scrollable_frame, style="WhiteCartFrame.TFrame", padding=10)
            item_frame.pack(fill="x", padx=5, pady=2)

            ttk.Label(item_frame, text=f"{item['name']} (ID: {item['id']})").pack(side="left")
            ttk.Label(item_frame, text=f"Qty: {quantity} {item['unit']}").pack(side="left", padx=10)
            ttk.Label(item_frame, text=f"${item_total:.2f}").pack(side="left", padx=10)

            ttk.Button(
                item_frame,
                text="Remove",
                command=lambda i=idx: self.remove_from_cart(i)
            ).pack(side="right")

        self.total_var.set(f"Total: ${total:.2f}")

    def remove_from_cart(self, index):
        self.cart.pop(index)
        self.update_cart()

    def create_account_frame(self):
        # Account header
        ttk.Label(self.account_frame, text="Account Details", font=("Arial", 16, "bold")).pack(pady=10)

        # Display user info
        info_frame = ttk.Frame(self.account_frame, style="WhiteFrame.TFrame", padding=10)
        info_frame.pack(fill="x", padx=10)

        ttk.Label(info_frame, text=f"Name: {self.user_data['name']}", font=("Arial", 12)).pack(anchor="w", pady=5)
        ttk.Label(info_frame, text=f"Email: {self.user_data['email']}", font=("Arial", 12)).pack(anchor="w", pady=5)

    def create_payment_frame(self):
        # Payment header
        ttk.Label(self.payment_frame, text="Payment Details", font=("Arial", 16, "bold")).pack(pady=10)

        # Form frame
        form_frame = ttk.Frame(self.payment_frame, style="WhiteFrame.TFrame", padding=10)
        form_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Customer details
        ttk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.name_var).grid(row=0, column=1, sticky="w", pady=5)

        ttk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="e", pady=5)
        self.email_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.email_var).grid(row=1, column=1, sticky="w", pady=5)

        ttk.Label(form_frame, text="Address:").grid(row=2, column=0, sticky="e", pady=5)
        self.address_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.address_var).grid(row=2, column=1, sticky="w", pady=5)

        # Payment method
        ttk.Label(form_frame, text="Payment Method:").grid(row=3, column=0, sticky="e", pady=5)
        self.payment_method_var = tk.StringVar(value="Card")
        ttk.Combobox(form_frame, textvariable=self.payment_method_var, values=["Card", "UPI"], state="readonly").grid(row=3, column=1, sticky="w", pady=5)

        # Card details (shown by default)
        self.card_frame = ttk.Frame(form_frame, style="WhiteFrame.TFrame")
        self.card_frame.grid(row=4, column=0, columnspan=2, pady=5)

        ttk.Label(self.card_frame, text="Card Number:").grid(row=0, column=0, sticky="e", pady=5)
        self.card_number_var = tk.StringVar()
        ttk.Entry(self.card_frame, textvariable=self.card_number_var).grid(row=0, column=1, sticky="w", pady=5)

        ttk.Label(self.card_frame, text="Expiry (MM/YY):").grid(row=1, column=0, sticky="e", pady=5)
        self.expiry_var = tk.StringVar()
        ttk.Entry(self.card_frame, textvariable=self.expiry_var).grid(row=1, column=1, sticky="w", pady=5)

        ttk.Label(self.card_frame, text="CVV:").grid(row=2, column=0, sticky="e", pady=5)
        self.cvv_var = tk.StringVar()
        ttk.Entry(self.card_frame, textvariable=self.cvv_var).grid(row=2, column=1, sticky="w", pady=5)

        # UPI details (hidden by default)
        self.upi_frame = ttk.Frame(form_frame, style="WhiteFrame.TFrame")

        ttk.Label(self.upi_frame, text="UPI ID:").grid(row=0, column=0, sticky="e", pady=5)
        self.upi_id_var = tk.StringVar()
        ttk.Entry(self.upi_frame, textvariable=self.upi_id_var).grid(row=0, column=1, sticky="w", pady=5)

        # Bind payment method change to update fields
        self.payment_method_var.trace("w", self.update_payment_fields)

        # Confirm payment button
        ttk.Button(form_frame, text="Confirm Payment", command=self.confirm_payment).grid(row=5, column=0, columnspan=2, pady=20)

    def update_payment_fields(self, *args):
        method = self.payment_method_var.get()
        if method == "Card":
            self.upi_frame.grid_forget()
            self.card_frame.grid(row=4, column=0, columnspan=2, pady=5)
        elif method == "UPI":
            self.card_frame.grid_forget()
            self.upi_frame.grid(row=4, column=0, columnspan=2, pady=5)

    def handle_pay_now(self):
        if not self.cart:
            messagebox.showerror("Error", "Cart is empty!")
            return
        # Reset payment fields
        self.name_var.set("")
        self.email_var.set("")
        self.address_var.set("")
        self.card_number_var.set("")
        self.expiry_var.set("")
        self.cvv_var.set("")
        self.upi_id_var.set("")
        self.payment_method_var.set("Card")
        self.show_payment()

    def handle_pay_on_delivery(self):
        if not self.cart:
            messagebox.showerror("Error", "Cart is empty!")
            return

        # Generate order confirmation
        total = sum(item["item"]["price"] * item["quantity"] for item in self.cart)
        receipt = f"Order Confirmation\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        receipt += f"Payment Method: Pay on Delivery\n\nItems:\n"
        for cart_item in self.cart:
            item = cart_item["item"]
            quantity = cart_item["quantity"]
            receipt += f"{item['name']} (ID: {item['id']}) - {quantity} {item['unit']} @ ${item['price']:.2f}/{item['unit']} = ${item['price'] * quantity:.2f}\n"
        receipt += f"\nTotal: ${total:.2f}\n\nYour order will be delivered soon!"

        messagebox.showinfo("Order Confirmed", receipt)
        self.cart = []
        self.update_cart()
        self.show_products()

    def confirm_payment(self):
        if not self.cart:
            messagebox.showerror("Error", "Cart is empty!")
            return

        # Validate customer details
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        address = self.address_var.get().strip()
        if not name or not email or not address:
            messagebox.showerror("Error", "Please fill in all customer details.")
            return

        # Basic email validation
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid email address.")
            return

        # Validate payment details
        method = self.payment_method_var.get()
        if method == "Card":
            card_number = self.card_number_var.get().strip()
            expiry = self.expiry_var.get().strip()
            cvv = self.cvv_var.get().strip()
            if not card_number or not expiry or not cvv:
                messagebox.showerror("Error", "Please fill in all card details.")
                return

            # Card number validation (16 digits, only numbers and spaces)
            card_number_clean = card_number.replace(" ", "")
            if not (len(card_number_clean) == 16 and card_number_clean.isdigit()):
                messagebox.showerror("Error", "Card number must be 16 digits.")
                return

            # Expiry validation (MM/YY format)
            expiry_pattern = r"^(0[1-9]|1[0-2])\/([0-9]{2})$"
            if not re.match(expiry_pattern, expiry):
                messagebox.showerror("Error", "Expiry must be in MM/YY format.")
                return

            # Check if card is expired
            month, year = map(int, expiry.split("/"))
            current_year = datetime.now().year % 100  # Last two digits of year
            current_month = datetime.now().month
            if year < current_year or (year == current_year and month < current_month):
                messagebox.showerror("Error", "Card has expired.")
                return

            # CVV validation (3 digits)
            if not (len(cvv) == 3 and cvv.isdigit()):
                messagebox.showerror("Error", "CVV must be 3 digits.")
                return

        elif method == "UPI":
            upi_id = self.upi_id_var.get().strip()
            if not upi_id:
                messagebox.showerror("Error", "Please fill in UPI ID.")
                return

            # UPI ID validation (basic format: something@something)
            upi_pattern = r"^[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}$"
            if not re.match(upi_pattern, upi_id):
                messagebox.showerror("Error", "Invalid UPI ID format.")
                return

        # Generate order confirmation
        total = sum(item["item"]["price"] * item["quantity"] for item in self.cart)
        receipt = f"Order Confirmation\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        receipt += f"Customer: {name}\nEmail: {email}\nAddress: {address}\n\n"
        receipt += f"Payment Method: {method}\n"
        if method == "Card":
            receipt += f"Card Number: {'*' * 12}{card_number_clean[-4:]}\n"
        else:
            receipt += f"UPI ID: {upi_id}\n"
        receipt += "\nItems:\n"
        for cart_item in self.cart:
            item = cart_item["item"]
            quantity = cart_item["quantity"]
            receipt += f"{item['name']} (ID: {item['id']}) - {quantity} {item['unit']} @ ${item['price']:.2f}/{item['unit']} = ${item['price'] * quantity:.2f}\n"
        receipt += f"\nTotal: ${total:.2f}\n\nThank you for your purchase!"

        messagebox.showinfo("Order Confirmed", receipt)
        self.cart = []
        self.update_cart()
        self.show_products()

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermarketApp(root)
    root.mainloop()