from itinerary.models import Activity

activities = [
    # Yala (Wild)
    (1, "Safari Tour", "Jetwing", 2000, "safari.jpg", "Explore Yala National Park"),
    (1, "Bird Watching", "Jetwing", 1000, "bird.jpg", "Spot unique bird species"),
    (1, "Wildlife Photography", "Jetwing", 3000, "wildlife.jpg", "Capture rare wildlife"),
    (1, "Camping", "Jetwing", 4000, "camping.jpg", "Stay overnight in the park"),
    (1, "Nature Walk", "Jetwing", 1500, "walk.jpg", "Guided walk through the jungle"),

    (1, "Safari Tour", "Authentic Ceylon", 2500, "safari.jpg", "Explore Yala National Park"),
    (1, "Bird Watching", "Authentic Ceylon", 1500, "bird.jpg", "Spot unique bird species"),
    (1, "Wildlife Photography", "Authentic Ceylon", 3500, "wildlife.jpg", "Capture rare wildlife"),
    (1, "Camping", "Authentic Ceylon", 5000, "camping.jpg", "Stay overnight in the park"),
    (1, "Nature Walk", "Authentic Ceylon", 2000, "walk.jpg", "Guided walk through the jungle"),

    (1, "Safari Tour", "Adventure Spirit", 3000, "safari.jpg", "Explore Yala National Park"),
    (1, "Bird Watching", "Adventure Spirit", 2000, "bird.jpg", "Spot unique bird species"),
    (1, "Wildlife Photography", "Adventure Spirit", 4000, "wildlife.jpg", "Capture rare wildlife"),
    (1, "Camping", "Adventure Spirit", 6000, "camping.jpg", "Stay overnight in the park"),
    (1, "Nature Walk", "Adventure Spirit", 2500, "walk.jpg", "Guided walk through the jungle"),

    (1, "Safari Tour", "Barefoot Luxury", 3500, "safari.jpg", "Explore Yala National Park"),
    (1, "Bird Watching", "Barefoot Luxury", 2500, "bird.jpg", "Spot unique bird species"),
    (1, "Wildlife Photography", "Barefoot Luxury", 4500, "wildlife.jpg", "Capture rare wildlife"),
    (1, "Camping", "Barefoot Luxury", 7000, "camping.jpg", "Stay overnight in the park"),
    (1, "Nature Walk", "Barefoot Luxury", 3000, "walk.jpg", "Guided walk through the jungle"),

    (1, "Safari Tour", "Normal", 1500, "safari.jpg", "Explore Yala National Park"),
    (1, "Bird Watching", "Normal", 800, "bird.jpg", "Spot unique bird species"),
    (1, "Wildlife Photography", "Normal", 2500, "wildlife.jpg", "Capture rare wildlife"),
    (1, "Camping", "Normal", 2000, "camping.jpg", "Stay overnight in the park"),
    (1, "Nature Walk", "Normal", 1000, "walk.jpg", "Guided walk through the jungle"),

    # Kumana (Wild)
    (2, "Safari Tour", "Jetwing", 2000, "safari.jpg", "Explore Kumana National Park"),
    (2, "Bird Watching", "Jetwing", 1000, "bird.jpg", "Spot unique bird species"),
    (2, "Wildlife Photography", "Jetwing", 3000, "wildlife.jpg", "Capture rare wildlife"),
    (2, "Camping", "Jetwing", 4000, "camping.jpg", "Stay overnight in the park"),
    (2, "Nature Walk", "Jetwing", 1500, "walk.jpg", "Guided walk through the jungle"),

    (2, "Safari Tour", "Authentic Ceylon", 2500, "safari.jpg", "Explore Kumana National Park"),
    (2, "Bird Watching", "Authentic Ceylon", 1500, "bird.jpg", "Spot unique bird species"),
    (2, "Wildlife Photography", "Authentic Ceylon", 3500, "wildlife.jpg", "Capture rare wildlife"),
    (2, "Camping", "Authentic Ceylon", 5000, "camping.jpg", "Stay overnight in the park"),
    (2, "Nature Walk", "Authentic Ceylon", 2000, "walk.jpg", "Guided walk through the jungle"),

    (2, "Safari Tour", "Adventure Spirit", 3000, "safari.jpg", "Explore Kumana National Park"),
    (2, "Bird Watching", "Adventure Spirit", 2000, "bird.jpg", "Spot unique bird species"),
    (2, "Wildlife Photography", "Adventure Spirit", 4000, "wildlife.jpg", "Capture rare wildlife"),
    (2, "Camping", "Adventure Spirit", 6000, "camping.jpg", "Stay overnight in the park"),
    (2, "Nature Walk", "Adventure Spirit", 2500, "walk.jpg", "Guided walk through the jungle"),

    (2, "Safari Tour", "Barefoot Luxury", 3500, "safari.jpg", "Explore Kumana National Park"),
    (2, "Bird Watching", "Barefoot Luxury", 2500, "bird.jpg", "Spot unique bird species"),
    (2, "Wildlife Photography", "Barefoot Luxury", 4500, "wildlife.jpg", "Capture rare wildlife"),
    (2, "Camping", "Barefoot Luxury", 7000, "camping.jpg", "Stay overnight in the park"),
    (2, "Nature Walk", "Barefoot Luxury", 3000, "walk.jpg", "Guided walk through the jungle"),

    (2, "Safari Tour", "Normal", 1500, "safari.jpg", "Explore Kumana National Park"),
    (2, "Bird Watching", "Normal", 800, "bird.jpg", "Spot unique bird species"),
    (2, "Wildlife Photography", "Normal", 2500, "wildlife.jpg", "Capture rare wildlife"),
    (2, "Camping", "Normal", 2000, "camping.jpg", "Stay overnight in the park"),
    (2, "Nature Walk", "Normal", 1000, "walk.jpg", "Guided walk through the jungle"),

    # Nuwara Eliya (Nature)
    (3, "Tea Tour", "Jetwing", 1000, "tea_tour.jpg", "Tour the famous tea plantations"),
    (3, "Waterfall Visit", "Jetwing", 1500, "waterfall.jpg", "Explore the beautiful waterfalls"),
    (3, "Nature Photography", "Jetwing", 2500, "nature.jpg", "Capture stunning nature landscapes"),
    (3, "Lake Visit", "Jetwing", 1200, "lake.jpg", "Relax by the serene Gregory Lake"),
    (3, "Hiking", "Jetwing", 1800, "hiking.jpg", "Hike through scenic mountain trails"),

    (3, "Tea Tour", "Authentic Ceylon", 1200, "tea_tour.jpg", "Tour the famous tea plantations"),
    (3, "Waterfall Visit", "Authentic Ceylon", 1800, "waterfall.jpg", "Explore the beautiful waterfalls"),
    (3, "Nature Photography", "Authentic Ceylon", 3000, "nature.jpg", "Capture stunning nature landscapes"),
    (3, "Lake Visit", "Authentic Ceylon", 1500, "lake.jpg", "Relax by the serene Gregory Lake"),
    (3, "Hiking", "Authentic Ceylon", 2200, "hiking.jpg", "Hike through scenic mountain trails"),

    (3, "Tea Tour", "Adventure Spirit", 1500, "tea_tour.jpg", "Tour the famous tea plantations"),
    (3, "Waterfall Visit", "Adventure Spirit", 2000, "waterfall.jpg", "Explore the beautiful waterfalls"),
    (3, "Nature Photography", "Adventure Spirit", 3500, "nature.jpg", "Capture stunning nature landscapes"),
    (3, "Lake Visit", "Adventure Spirit", 2000, "lake.jpg", "Relax by the serene Gregory Lake"),
    (3, "Hiking", "Adventure Spirit", 3000, "hiking.jpg", "Hike through scenic mountain trails"),

    (3, "Tea Tour", "Barefoot Luxury", 2000, "tea_tour.jpg", "Tour the famous tea plantations"),
    (3, "Waterfall Visit", "Barefoot Luxury", 2500, "waterfall.jpg", "Explore the beautiful waterfalls"),
    (3, "Nature Photography", "Barefoot Luxury", 4000, "nature.jpg", "Capture stunning nature landscapes"),
    (3, "Lake Visit", "Barefoot Luxury", 2500, "lake.jpg", "Relax by the serene Gregory Lake"),
    (3, "Hiking", "Barefoot Luxury", 3500, "hiking.jpg", "Hike through scenic mountain trails"),

    (3, "Tea Tour", "Normal", 1000, "tea_tour.jpg", "Tour the famous tea plantations"),
    (3, "Waterfall Visit", "Normal", 1200, "waterfall.jpg", "Explore the beautiful waterfalls"),
    (3, "Nature Photography", "Normal", 2500, "nature.jpg", "Capture stunning nature landscapes"),
    (3, "Lake Visit", "Normal", 1000, "lake.jpg", "Relax by the serene Gregory Lake"),
    (3, "Hiking", "Normal", 1500, "hiking.jpg", "Hike through scenic mountain trails"),

    # Colombo (City)
    (4, "City Tour", "Jetwing", 2000, "city_tour.jpg", "Explore the historical sites of Colombo"),
    (4, "Shopping", "Jetwing", 1500, "shopping.jpg", "Visit the famous shopping malls"),
    (4, "Museum Visit", "Jetwing", 1800, "museum.jpg", "Explore the National Museum"),
    (4, "Food Tour", "Jetwing", 2500, "food_tour.jpg", "Taste Sri Lanka's best cuisines"),
    (4, "Cultural Show", "Jetwing", 2200, "culture_show.jpg", "Enjoy a traditional cultural performance"),

    (4, "City Tour", "Authentic Ceylon", 2500, "city_tour.jpg", "Explore the historical sites of Colombo"),
    (4, "Shopping", "Authentic Ceylon", 1800, "shopping.jpg", "Visit the famous shopping malls"),
    (4, "Museum Visit", "Authentic Ceylon", 2000, "museum.jpg", "Explore the National Museum"),
    (4, "Food Tour", "Authentic Ceylon", 3000, "food_tour.jpg", "Taste Sri Lanka's best cuisines"),
    (4, "Cultural Show", "Authentic Ceylon", 2800, "culture_show.jpg", "Enjoy a traditional cultural performance"),

    (4, "City Tour", "Adventure Spirit", 3000, "city_tour.jpg", "Explore the historical sites of Colombo"),
    (4, "Shopping", "Adventure Spirit", 2500, "shopping.jpg", "Visit the famous shopping malls"),
    (4, "Museum Visit", "Adventure Spirit", 3000, "museum.jpg", "Explore the National Museum"),
    (4, "Food Tour", "Adventure Spirit", 3500, "food_tour.jpg", "Taste Sri Lanka's best cuisines"),
    (4, "Cultural Show", "Adventure Spirit", 3200, "culture_show.jpg", "Enjoy a traditional cultural performance"),

    (4, "City Tour", "Barefoot Luxury", 3500, "city_tour.jpg", "Explore the historical sites of Colombo"),
    (4, "Shopping", "Barefoot Luxury", 3000, "shopping.jpg", "Visit the famous shopping malls"),
    (4, "Museum Visit", "Barefoot Luxury", 3500, "museum.jpg", "Explore the National Museum"),
    (4, "Food Tour", "Barefoot Luxury", 4000, "food_tour.jpg", "Taste Sri Lanka's best cuisines"),
    (4, "Cultural Show", "Barefoot Luxury", 3800, "culture_show.jpg", "Enjoy a traditional cultural performance"),

    (4, "City Tour", "Normal", 1500, "city_tour.jpg", "Explore the historical sites of Colombo"),
    (4, "Shopping", "Normal", 1000, "shopping.jpg", "Visit the famous shopping malls"),
    (4, "Museum Visit", "Normal", 1500, "museum.jpg", "Explore the National Museum"),
    (4, "Food Tour", "Normal", 2000, "food_tour.jpg", "Taste Sri Lanka's best cuisines"),
    (4, "Cultural Show", "Normal", 1800, "culture_show.jpg", "Enjoy a traditional cultural performance"),
]

for location_id, name, category, price, image_url, description in activities:
    Activity.objects.create(location_id=location_id, name=name, category=category, price=price, image_url=image_url, description=description)
  












  ##dailyrange data range enter to db

  python manage.py shell

from itinerary.models import DailyBudgetRange

start_min = 15
end_max = 5200
increment = 5

daily_budget_ranges = []

for min_value in range(start_min, end_max + 1, increment):
    max_value = min_value + increment - 1
    daily_budget = max_value
    daily_budget_range = DailyBudgetRange(
        range_min=min_value,
        range_max=max_value,
        daily_budget=daily_budget
    )
    daily_budget_ranges.append(daily_budget_range)

DailyBudgetRange.objects.bulk_create(daily_budget_ranges)

print("Daily budget ranges added successfully.")
print(DailyBudgetRange.objects.count())  # Verify total entries
print(DailyBudgetRange.objects.first())  # Check first entry
print(DailyBudgetRange.objects.last())   # Check last entry





print(list(DailyBudgetRange.objects.all()[:5]))  # Shows first 5 entries












<!-- locations adding  -->
<!-- 




python manage.py shell

from itinerary.models import Location

from itinerary.models import Location

cities = [
    {"name": "Colombo", "image_url": "https://via.placeholder.com/150?text=Colombo", "notes": "Capital city of Sri Lanka, a major port and economic hub."},
    {"name": "Kandy", "image_url": "https://via.placeholder.com/150?text=Kandy", "notes": "Historic city, known for the Temple of the Tooth."},
    {"name": "Galle", "image_url": "https://via.placeholder.com/150?text=Galle", "notes": "Historic city with a famous Dutch fort."},
    {"name": "Nuwara Eliya", "image_url": "https://via.placeholder.com/150?text=Nuwara+Eliya", "notes": "A hill station known for its cool climate and tea plantations."},
    {"name": "Negombo", "image_url": "https://via.placeholder.com/150?text=Negombo", "notes": "Coastal city with a major fishing industry and beaches."},
    {"name": "Anuradhapura", "image_url": "https://via.placeholder.com/150?text=Anuradhapura", "notes": "Ancient capital of Sri Lanka, home to many Buddhist monuments."},
    {"name": "Sigiriya", "image_url": "https://via.placeholder.com/150?text=Sigiriya", "notes": "Famous for the Sigiriya rock fortress, a UNESCO World Heritage site."},
    {"name": "Ella", "image_url": "https://via.placeholder.com/150?text=Ella", "notes": "Small town known for stunning views and tea plantations."},
    {"name": "Trincomalee", "image_url": "https://via.placeholder.com/150?text=Trincomalee", "notes": "A coastal town known for its natural harbor and beaches."},
    {"name": "Jaffna", "image_url": "https://via.placeholder.com/150?text=Jaffna", "notes": "Located in the north, known for its Tamil culture and heritage."},
    {"name": "Matara", "image_url": "https://via.placeholder.com/150?text=Matara", "notes": "Coastal city with beautiful beaches and historical landmarks."},
    {"name": "Hikkaduwa", "image_url": "https://via.placeholder.com/150?text=Hikkaduwa", "notes": "Famous for its coral reefs and vibrant beach life."},
    {"name": "Mannar", "image_url": "https://via.placeholder.com/150?text=Mannar", "notes": "A town in the northwest, known for its salt pans and fishing industry."},
    {"name": "Ratnapura", "image_url": "https://via.placeholder.com/150?text=Ratnapura", "notes": "The gem capital of Sri Lanka, known for its gem mines."},
    {"name": "Kegalle", "image_url": "https://via.placeholder.com/150?text=Kegalle", "notes": "A town surrounded by tropical forests and home to the Pinnawala Elephant Orphanage."},
    {"name": "Badulla", "image_url": "https://via.placeholder.com/150?text=Badulla", "notes": "A town in the Uva Province, known for its scenic landscapes."},
    {"name": "Polonnaruwa", "image_url": "https://via.placeholder.com/150?text=Polonnaruwa", "notes": "Ancient city known for its well-preserved ruins and Buddhist statues."},
    {"name": "Kurunegala", "image_url": "https://via.placeholder.com/150?text=Kurunegala", "notes": "A city with historical significance and beautiful landscapes."},
    {"name": "Dambulla", "image_url": "https://via.placeholder.com/150?text=Dambulla", "notes": "Known for its cave temples and stunning Buddha statues."},
    {"name": "Beruwala", "image_url": "https://via.placeholder.com/150?text=Beruwala", "notes": "A coastal town with beautiful beaches and resorts."},
    {"name": "Weligama", "image_url": "https://via.placeholder.com/150?text=Weligama", "notes": "A popular beach destination known for surfing."},
    {"name": "Mirissa", "image_url": "https://via.placeholder.com/150?text=Mirissa", "notes": "A small town known for its beaches and whale watching."},
    {"name": "Puttalam", "image_url": "https://via.placeholder.com/150?text=Puttalam", "notes": "A coastal town known for its fishing industry and lagoons."},
    {"name": "Arugam Bay", "image_url": "https://via.placeholder.com/150?text=Arugam+Bay", "notes": "A famous beach for surfing on the east coast of Sri Lanka."},
    {"name": "Kalpitiya", "image_url": "https://via.placeholder.com/150?text=Kalpitiya", "notes": "A coastal town known for its kite surfing and wild lagoons."},
    {"name": "Hambantota", "image_url": "https://via.placeholder.com/150?text=Hambantota", "notes": "A port city known for its beaches and national parks."}
]

# Adding cities to the Location model
for city in cities:
    Location.objects.create(
        name=city["name"],
        image_url=city["image_url"],
        notes=city["notes"]
    )

print("All cities added successfully!") -->










# activity colombo

from itinerary.models import Activity, Location  # Make sure to import Activity and Location

# Add Colombo location if it doesn't already exist
colombo = Location.objects.create(
    name="Colombo",
    image_url="https://via.placeholder.com/150?text=Colombo",
    notes="Capital city of Sri Lanka, a major port and economic hub."
)

# Activity data for Colombo with varying prices and categories
activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the National Museum", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the rich history of Sri Lanka at the National Museum.", "price_range": "Low", "activity_rank": 1},
    {"name": "Tour of Galle Face Green", "category": "Cultural and Heritage Tours", "price": 20, "description": "A historic landmark and seaside park offering stunning views.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Old Dutch Hospital Visit", "category": "Cultural and Heritage Tours", "price": 15, "description": "A colonial-era hospital turned into a shopping precinct.", "price_range": "Low", "activity_rank": 3},
    {"name": "Colombo Fort Tour", "category": "Cultural and Heritage Tours", "price": 30, "description": "Explore the colonial buildings in the Colombo Fort area.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Gangaramaya Temple Visit", "category": "Cultural and Heritage Tours", "price": 40, "description": "Visit the famous Buddhist temple with a museum and a cultural center.", "price_range": "High", "activity_rank": 5},
    
    # Nature and Wildlife Tours
    {"name": "Visit Dehiwala Zoo", "category": "Nature and Wildlife Tours", "price": 8, "description": "Explore the animals and wildlife at the Dehiwala Zoo.", "price_range": "Low", "activity_rank": 1},
    {"name": "Sri Lanka Nature Reserve Tour", "category": "Nature and Wildlife Tours", "price": 25, "description": "A guided nature walk through Sri Lanka's tropical forests.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Muthurajawela Marsh Boat Safari", "category": "Nature and Wildlife Tours", "price": 15, "description": "Take a boat safari through the Muthurajawela Marsh and observe diverse bird species.", "price_range": "Low", "activity_rank": 3},
    {"name": "Bird Watching at Attidiya Wetlands", "category": "Nature and Wildlife Tours", "price": 35, "description": "Discover a variety of bird species at the Attidiya Wetlands.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Whale Watching Trip from Colombo", "category": "Nature and Wildlife Tours", "price": 70, "description": "Go on a whale watching excursion in the Indian Ocean.", "price_range": "High", "activity_rank": 5},
    
    # Beach and Coastal Tours
    {"name": "Mount Lavinia Beach Visit", "category": "Beach and Coastal Tours", "price": 5, "description": "Relax and swim at one of Colombo's popular beaches.", "price_range": "Low", "activity_rank": 1},
    {"name": "Negombo Beach Tour", "category": "Beach and Coastal Tours", "price": 20, "description": "Explore the beautiful beaches of Negombo, known for its relaxing atmosphere.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Sri Lanka Coastal Walk", "category": "Beach and Coastal Tours", "price": 12, "description": "Take a scenic walk along Colombo’s coastline.", "price_range": "Low", "activity_rank": 3},
    {"name": "Snorkeling at Colombo Beach", "category": "Beach and Coastal Tours", "price": 25, "description": "Snorkel in the clear waters and explore underwater life.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Private Beach Party in Colombo", "category": "Beach and Coastal Tours", "price": 50, "description": "Enjoy a private beach party with music, drinks, and sunset views.", "price_range": "High", "activity_rank": 5},
    
    # Adventure Tours
    {"name": "Colombo City Cycling Tour", "category": "Adventure Tours", "price": 15, "description": "Explore Colombo on a guided cycling tour through the city's streets.", "price_range": "Low", "activity_rank": 1},
    {"name": "Colombo Ziplining Adventure", "category": "Adventure Tours", "price": 35, "description": "Experience the thrill of ziplining through Colombo’s jungle areas.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Climbing the Colombo Hill", "category": "Adventure Tours", "price": 10, "description": "Hike to the top of a hill for panoramic views of the city.", "price_range": "Low", "activity_rank": 3},
    {"name": "Jet Ski at Colombo Beach", "category": "Adventure Tours", "price": 40, "description": "Enjoy a thrilling ride on a jet ski along the coast.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Skydiving Over Colombo", "category": "Adventure Tours", "price": 150, "description": "Go skydiving for an exhilarating aerial view of Colombo.", "price_range": "High", "activity_rank": 5},
    
    # General Activities
    {"name": "City Sightseeing Tour", "category": "General", "price": 20, "description": "Take a guided city sightseeing tour and explore Colombo's top attractions.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Colombo Street Food Tour", "category": "General", "price": 10, "description": "Explore the local street food scene in Colombo.", "price_range": "Low", "activity_rank": 2},
    {"name": "Shopping at Odel Mall", "category": "General", "price": 30, "description": "Visit Colombo's famous Odel Mall for shopping and leisure.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Evening Boat Ride at Beira Lake", "category": "General", "price": 15, "description": "Relax and take a peaceful boat ride in Beira Lake.", "price_range": "Low", "activity_rank": 4},
    {"name": "Visit Colombo Night Market", "category": "General", "price": 25, "description": "Experience the vibrant atmosphere of Colombo's Night Market.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Colombo
for activity in activities_data:
    Activity.objects.create(
        location=colombo,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# hambantota
from itinerary.models import Location, Activity

# Add Hambantota location
hambantota = Location.objects.create(
    name="Hambantota",
    image_url="https://via.placeholder.com/150?text=Hambantota",
    notes="A coastal city in the southern part of Sri Lanka, known for its beaches and wildlife sanctuaries."
)

# Activity data for Hambantota with varying prices and categories
activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Yala National Park Museum", "category": "Cultural and Heritage Tours", "price": 15, "description": "Explore the rich history and culture of the Yala region at the national park museum.", "price_range": "Low", "activity_rank": 1},
    {"name": "Tissamaharama Raja Maha Vihara Visit", "category": "Cultural and Heritage Tours", "price": 20, "description": "Visit the historical Tissamaharama Buddhist temple, one of the oldest in the region.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Buddhist Temple in Hambantota", "category": "Cultural and Heritage Tours", "price": 12, "description": "A guided tour of a local Buddhist temple in Hambantota.", "price_range": "Low", "activity_rank": 3},
    {"name": "Sithulpawwa Temple Visit", "category": "Cultural and Heritage Tours", "price": 30, "description": "Explore the ancient rock temple, with stunning views and historical significance.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit Hambantota Clock Tower", "category": "Cultural and Heritage Tours", "price": 25, "description": "A historical site that marks the colonial past of Hambantota.", "price_range": "High", "activity_rank": 5},
    
    # Nature and Wildlife Tours
    {"name": "Yala National Park Safari", "category": "Nature and Wildlife Tours", "price": 40, "description": "Go on a thrilling safari in one of Sri Lanka's most famous national parks, home to leopards, elephants, and more.", "price_range": "High", "activity_rank": 1},
    {"name": "Kumana National Park Bird Watching", "category": "Nature and Wildlife Tours", "price": 15, "description": "Observe a wide variety of bird species at the Kumana National Park.", "price_range": "Low", "activity_rank": 2},
    {"name": "Bundala National Park Safari", "category": "Nature and Wildlife Tours", "price": 25, "description": "Explore the biodiversity of Bundala National Park with a guided safari.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Rekawa Turtle Sanctuary Visit", "category": "Nature and Wildlife Tours", "price": 10, "description": "Visit the turtle sanctuary to learn about turtle conservation efforts and spot nesting turtles.", "price_range": "Low", "activity_rank": 4},
    {"name": "Wildlife Watching in Hambantota Lagoon", "category": "Nature and Wildlife Tours", "price": 20, "description": "A boat tour through the lagoon, offering a chance to spot birds and other wildlife.", "price_range": "Medium", "activity_rank": 5},
    
    # Beach and Coastal Tours
    {"name": "Visit Tangalle Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Relax on the pristine beach of Tangalle, perfect for sunbathing and swimming.", "price_range": "Low", "activity_rank": 1},
    {"name": "Weligama Beach Surfing", "category": "Beach and Coastal Tours", "price": 20, "description": "Learn surfing at one of Sri Lanka's most famous beaches for beginners.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Hiriketiya Beach Relaxation", "category": "Beach and Coastal Tours", "price": 15, "description": "Enjoy a peaceful day at Hiriketiya Beach, known for its calm waters and scenic beauty.", "price_range": "Low", "activity_rank": 3},
    {"name": "Scuba Diving in Weligama Bay", "category": "Beach and Coastal Tours", "price": 40, "description": "Dive into the crystal-clear waters of Weligama Bay and discover vibrant marine life.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Private Beach Picnic in Hambantota", "category": "Beach and Coastal Tours", "price": 50, "description": "Enjoy a private beach picnic with local delicacies and sunset views.", "price_range": "High", "activity_rank": 5},
    
    # Adventure Tours
    {"name": "Cycling Tour in Hambantota", "category": "Adventure Tours", "price": 15, "description": "Embark on an exciting cycling tour through the rural areas surrounding Hambantota.", "price_range": "Low", "activity_rank": 1},
    {"name": "Yala Jeep Safari", "category": "Adventure Tours", "price": 30, "description": "Get close to wildlife in Yala National Park during a thrilling jeep safari.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Trekking in Kumana National Park", "category": "Adventure Tours", "price": 20, "description": "A guided trek through Kumana National Park, ideal for nature lovers and adventure seekers.", "price_range": "Low", "activity_rank": 3},
    {"name": "Snorkeling at Tangalle", "category": "Adventure Tours", "price": 25, "description": "Explore the underwater world of Tangalle with a guided snorkeling tour.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Quad Biking in Hambantota", "category": "Adventure Tours", "price": 60, "description": "Feel the thrill of quad biking through the sandy terrains of Hambantota.", "price_range": "High", "activity_rank": 5},
    
    # General Activities
    {"name": "Visit Hambantota Port", "category": "General", "price": 10, "description": "Tour one of the largest and busiest ports in Sri Lanka, and learn about its operations.", "price_range": "Low", "activity_rank": 1},
    {"name": "Shopping at Hambantota Market", "category": "General", "price": 15, "description": "Explore the local markets and shop for authentic Sri Lankan crafts and souvenirs.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Evening at Hambantota Beach", "category": "General", "price": 5, "description": "Relax and watch the sunset at the beautiful Hambantota beach.", "price_range": "Low", "activity_rank": 3},
    {"name": "Hambantota City Tour", "category": "General", "price": 20, "description": "Explore the city’s cultural landmarks and key attractions.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Dinner at a Beachside Restaurant", "category": "General", "price": 35, "description": "Enjoy a seaside dinner with fresh seafood and local delicacies.", "price_range": "High", "activity_rank": 5},
]

# Insert activities into the database for Hambantota
for activity in activities_data:
    Activity.objects.create(
        location=hambantota,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )





# mirissa puttalama

from itinerary.models import Location, Activity

# Puttalam Location (Checking if already exists)
puttalam, created = Location.objects.get_or_create(
    name="Puttalam",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Puttalam",
        "notes": "Puttalam is known for its beautiful beaches and salt production industry."
    }
)

# Activity data for Puttalam with varying prices and categories
puttalam_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Puttalam Fort", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the historical Puttalam Fort, built during the Dutch colonial period.", "price_range": "Low", "activity_rank": 1},
    {"name": "Puttalam Buddhist Temple Visit", "category": "Cultural and Heritage Tours", "price": 8, "description": "Visit a significant Buddhist temple in the heart of Puttalam.", "price_range": "Low", "activity_rank": 2},
    {"name": "Explore Munneswaram Temple", "category": "Cultural and Heritage Tours", "price": 15, "description": "The Munneswaram Temple is one of the oldest and most sacred Hindu temples in Sri Lanka.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Puttalam Church Visit", "category": "Cultural and Heritage Tours", "price": 5, "description": "Visit the local church and learn about its historical significance.", "price_range": "Low", "activity_rank": 4},
    {"name": "Historical Sites Tour of Puttalam", "category": "Cultural and Heritage Tours", "price": 12, "description": "A guided tour of Puttalam's historical sites and monuments.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Wilpattu National Park Safari", "category": "Nature and Wildlife Tours", "price": 30, "description": "Go on a safari in the famous Wilpattu National Park, home to diverse wildlife including leopards and elephants.", "price_range": "High", "activity_rank": 1},
    {"name": "Puttalam Lagoon Boat Ride", "category": "Nature and Wildlife Tours", "price": 20, "description": "Take a boat ride through the Puttalam Lagoon, home to rich biodiversity and birdlife.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Bird Watching at Puttalam", "category": "Nature and Wildlife Tours", "price": 15, "description": "Enjoy bird watching in the Puttalam lagoon, a hotspot for migratory birds.", "price_range": "Low", "activity_rank": 3},
    {"name": "Salt Field Tour", "category": "Nature and Wildlife Tours", "price": 10, "description": "Visit the salt fields in Puttalam and learn about the process of salt production.", "price_range": "Low", "activity_rank": 4},
    {"name": "Fishing Tour in Puttalam", "category": "Nature and Wildlife Tours", "price": 18, "description": "Join a local fishing tour to explore Puttalam's traditional fishing methods.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Puttalam Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Enjoy the serene environment of Puttalam Beach, a perfect spot for relaxation.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit Kalpitiya Beach", "category": "Beach and Coastal Tours", "price": 10, "description": "Explore the beautiful Kalpitiya Beach, perfect for swimming and sunbathing.", "price_range": "Low", "activity_rank": 2},
    {"name": "Snorkeling at Puttalam", "category": "Beach and Coastal Tours", "price": 25, "description": "Snorkel in the clear waters of Puttalam and discover the underwater world.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Kite Surfing in Kalpitiya", "category": "Beach and Coastal Tours", "price": 40, "description": "Try kite surfing in Kalpitiya, one of the best locations in Sri Lanka for the sport.", "price_range": "High", "activity_rank": 4},
    {"name": "Puttalam Beach Sunset", "category": "Beach and Coastal Tours", "price": 8, "description": "Watch a beautiful sunset at Puttalam Beach.", "price_range": "Low", "activity_rank": 5},

    # Adventure Tours
    {"name": "Kayaking in Puttalam Lagoon", "category": "Adventure Tours", "price": 20, "description": "Kayak through the peaceful Puttalam Lagoon and enjoy the surrounding nature.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Jet Skiing in Puttalam", "category": "Adventure Tours", "price": 30, "description": "Experience the thrill of jet skiing in the calm waters of Puttalam.", "price_range": "High", "activity_rank": 2},
    {"name": "Quad Biking in Puttalam", "category": "Adventure Tours", "price": 35, "description": "Embark on a quad biking adventure across Puttalam's rugged terrain.", "price_range": "High", "activity_rank": 3},
    {"name": "Sandboarding in Puttalam", "category": "Adventure Tours", "price": 25, "description": "Try sandboarding on the dunes around Puttalam Beach.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Fishing Expedition in Puttalam", "category": "Adventure Tours", "price": 20, "description": "Join a local fisherman on an expedition to catch local fish species.", "price_range": "Low", "activity_rank": 5},

    # General Activities
    {"name": "Puttalam Market Tour", "category": "General", "price": 8, "description": "Visit the local market and explore Sri Lanka's fresh produce and local crafts.", "price_range": "Low", "activity_rank": 1},
    {"name": "Cultural Evening in Puttalam", "category": "General", "price": 15, "description": "Experience the local culture through music and dance performances in Puttalam.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Puttalam Village Visit", "category": "General", "price": 12, "description": "Visit the local village and learn about the traditions and lifestyle of the community.", "price_range": "Low", "activity_rank": 3},
    {"name": "Dinner at Puttalam Beach Restaurant", "category": "General", "price": 30, "description": "Indulge in a fresh seafood dinner by the beach in Puttalam.", "price_range": "High", "activity_rank": 4},
    {"name": "Yoga Retreat in Puttalam", "category": "General", "price": 50, "description": "Join a yoga retreat by the beach and rejuvenate your mind and body.", "price_range": "High", "activity_rank": 5},
]

# Insert activities into the database for Puttalam
for activity in puttalam_activities_data:
    Activity.objects.create(
        location=puttalam,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Mirissa Location (Checking if already exists)
mirissa, created = Location.objects.get_or_create(
    name="Mirissa",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Mirissa",
        "notes": "Mirissa is known for its beaches, whale watching, and relaxed vibe."
    }
)

# Activity data for Mirissa with varying prices and categories
mirissa_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Mirissa Buddhist Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "A visit to the serene Buddhist temple offering spiritual solace.", "price_range": "Low", "activity_rank": 1},
    {"name": "Mirissa Historical Sites Tour", "category": "Cultural and Heritage Tours", "price": 15, "description": "Discover the history and culture of Mirissa through its ancient temples and sites.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Explore Galle Fort", "category": "Cultural and Heritage Tours", "price": 20, "description": "Visit Galle Fort, a UNESCO World Heritage Site, just a short drive from Mirissa.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit St. Mary's Church", "category": "Cultural and Heritage Tours", "price": 5, "description": "Explore the charming St. Mary's Church in the heart of Mirissa.", "price_range": "Low", "activity_rank": 4},
    {"name": "Visit Koggala Buddhist Temple", "category": "Cultural and Heritage Tours", "price": 12, "description": "A serene and peaceful temple located just outside Mirissa.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Whale Watching Tour in Mirissa", "category": "Nature and Wildlife Tours", "price": 50, "description": "Go on a thrilling whale watching tour, where you can spot blue whales and dolphins.", "price_range": "High", "activity_rank": 1},
    {"name": "Snorkeling at Mirissa Beach", "category": "Nature and Wildlife Tours", "price": 25, "description": "Enjoy snorkeling in the clear, warm waters of Mirissa beach, home to colorful marine life.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Mirissa Reef Exploration", "category": "Nature and Wildlife Tours", "price": 30, "description": "Explore the vibrant coral reefs off the coast of Mirissa.", "price_range": "High", "activity_rank": 3},
    {"name": "Whale Watching Boat Ride", "category": "Nature and Wildlife Tours", "price": 40, "description": "Take a boat ride for an exciting whale watching experience.", "price_range": "High", "activity_rank": 4},
    {"name": "Turtle Watching in Mirissa", "category": "Nature and Wildlife Tours", "price": 20, "description": "Observe sea turtles nesting along the Mirissa coastline.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Mirissa Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Unwind on the tranquil beach of Mirissa.", "price_range": "Low", "activity_rank": 1},
    {"name": "Surfing in Mirissa", "category": "Beach and Coastal Tours", "price": 30, "description": "Learn surfing at one of the most popular surf spots in Sri Lanka.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Sunset at Mirissa", "category": "Beach and Coastal Tours", "price": 8, "description": "Watch the stunning sunset over the bay at Mirissa.", "price_range": "Low", "activity_rank": 3},
    {"name": "Scuba Diving in Mirissa", "category": "Beach and Coastal Tours", "price": 35, "description": "Explore the underwater world of Mirissa with scuba diving.", "price_range": "High", "activity_rank": 4},
    {"name": "Night Fishing in Mirissa", "category": "Beach and Coastal Tours", "price": 20, "description": "Go night fishing in the warm waters of Mirissa.", "price_range": "Medium", "activity_rank": 5},

    # Adventure Tours
    {"name": "Hiking to Mirissa Viewpoint", "category": "Adventure Tours", "price": 10, "description": "Hike to the top of Mirissa Hill for stunning views of the bay.", "price_range": "Low", "activity_rank": 1},
    {"name": "Jet Skiing in Mirissa", "category": "Adventure Tours", "price": 25, "description": "Enjoy jet skiing in the crystal-clear waters of Mirissa.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Kayaking in Mirissa", "category": "Adventure Tours", "price": 20, "description": "Kayak through the calm, scenic waters of Mirissa beach.", "price_range": "Low", "activity_rank": 3},
    {"name": "Stand-Up Paddleboarding", "category": "Adventure Tours", "price": 30, "description": "Learn stand-up paddleboarding in Mirissa.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Paragliding in Mirissa", "category": "Adventure Tours", "price": 40, "description": "Take flight and enjoy panoramic views of Mirissa from the sky.", "price_range": "High", "activity_rank": 5},

    # General Activities
    {"name": "Mirissa Local Market Tour", "category": "General", "price": 12, "description": "Explore the local market and sample fresh tropical fruits and seafood.", "price_range": "Low", "activity_rank": 1},
    {"name": "Cultural Evening in Mirissa", "category": "General", "price": 15, "description": "Join a local cultural performance featuring traditional Sri Lankan music and dance.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Yoga Retreat in Mirissa", "category": "General", "price": 50, "description": "Relax your mind and body at a yoga retreat in Mirissa.", "price_range": "High", "activity_rank": 3},
    {"name": "Seafood Dinner at Mirissa Beach", "category": "General", "price": 30, "description": "Enjoy a fresh seafood dinner by the ocean.", "price_range": "High", "activity_rank": 4},
    {"name": "Nightlife in Mirissa", "category": "General", "price": 15, "description": "Experience the laid-back nightlife of Mirissa with local bars and music.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Mirissa
for activity in mirissa_activities_data:
    Activity.objects.create(
        location=mirissa,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )









# weligama beruwla

from itinerary.models import Location, Activity

# Weligama Location (Checking if already exists)
weligama, created = Location.objects.get_or_create(
    name="Weligama",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Weligama",
        "notes": "Weligama is famous for its surfing beaches, relaxed vibe, and cultural experiences."
    }
)

# Activity data for Weligama with varying prices and categories
weligama_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Weligama Buddhist Temple", "category": "Cultural and Heritage Tours", "price": 8, "description": "A visit to the serene Buddhist temple offering spiritual insights.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore Galle Fort", "category": "Cultural and Heritage Tours", "price": 15, "description": "Visit the UNESCO World Heritage Site, Galle Fort, located nearby.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Stilt Fishing Experience", "category": "Cultural and Heritage Tours", "price": 10, "description": "Watch and learn about the unique traditional stilt fishing technique.", "price_range": "Low", "activity_rank": 3},
    {"name": "Visit Historical Temples", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit some of the ancient temples around Weligama.", "price_range": "Low", "activity_rank": 4},
    {"name": "Cultural Tour of Weligama", "category": "Cultural and Heritage Tours", "price": 18, "description": "A guided cultural tour showcasing the rich history and traditions of Weligama.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Whale Watching in Weligama", "category": "Nature and Wildlife Tours", "price": 50, "description": "Go on a whale watching excursion, a popular activity in Weligama.", "price_range": "High", "activity_rank": 1},
    {"name": "Snorkeling in Weligama", "category": "Nature and Wildlife Tours", "price": 25, "description": "Snorkel in the crystal-clear waters of Weligama Bay, home to diverse marine life.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Turtle Watching Tour", "category": "Nature and Wildlife Tours", "price": 20, "description": "Observe the endangered sea turtles in Weligama's coastal waters.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Mangrove Boat Ride", "category": "Nature and Wildlife Tours", "price": 15, "description": "Take a boat ride through the serene mangroves near Weligama.", "price_range": "Low", "activity_rank": 4},
    {"name": "Safari at Kumana National Park", "category": "Nature and Wildlife Tours", "price": 40, "description": "Take a safari tour at Kumana National Park to spot diverse wildlife including elephants and leopards.", "price_range": "High", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Weligama Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Unwind on the beautiful beach of Weligama, famous for its surf breaks.", "price_range": "Low", "activity_rank": 1},
    {"name": "Surfing in Weligama", "category": "Beach and Coastal Tours", "price": 30, "description": "Learn or enjoy surfing at one of Sri Lanka's best surf spots.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Sunset at Weligama Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Enjoy a serene sunset over the beach while sipping a refreshing drink.", "price_range": "Low", "activity_rank": 3},
    {"name": "Stand-Up Paddleboarding in Weligama", "category": "Beach and Coastal Tours", "price": 15, "description": "Experience stand-up paddleboarding on the calm waters of Weligama Bay.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Scuba Diving in Weligama", "category": "Beach and Coastal Tours", "price": 35, "description": "Explore the underwater beauty of Weligama's coastal waters with a scuba diving adventure.", "price_range": "High", "activity_rank": 5},

    # Adventure Tours
    {"name": "Kayaking in Weligama Bay", "category": "Adventure Tours", "price": 18, "description": "Enjoy kayaking in the calm waters of Weligama Bay.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Jet Skiing in Weligama", "category": "Adventure Tours", "price": 30, "description": "Experience the thrill of jet skiing in Weligama's warm waters.", "price_range": "High", "activity_rank": 2},
    {"name": "Quad Biking in Weligama", "category": "Adventure Tours", "price": 35, "description": "Take a quad bike ride around Weligama's coastal areas.", "price_range": "High", "activity_rank": 3},
    {"name": "Ziplining in Weligama", "category": "Adventure Tours", "price": 40, "description": "Experience the thrill of ziplining over the lush landscape of Weligama.", "price_range": "High", "activity_rank": 4},
    {"name": "Trekking to Weligama Viewpoint", "category": "Adventure Tours", "price": 12, "description": "Hike up to the Weligama Viewpoint for panoramic views of the coastline.", "price_range": "Low", "activity_rank": 5},

    # General Activities
    {"name": "Weligama Market Tour", "category": "General", "price": 8, "description": "Explore the local market and sample Sri Lanka's fresh produce and local delicacies.", "price_range": "Low", "activity_rank": 1},
    {"name": "Cultural Evening in Weligama", "category": "General", "price": 15, "description": "Join a cultural evening showcasing traditional Sri Lankan music and dance.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Yoga in Weligama", "category": "General", "price": 20, "description": "Relax your mind and body with a yoga session in the peaceful environment of Weligama.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Seafood Dinner in Weligama", "category": "General", "price": 25, "description": "Indulge in a delicious seafood dinner at one of the many beachfront restaurants.", "price_range": "High", "activity_rank": 4},
    {"name": "Nightlife in Weligama", "category": "General", "price": 10, "description": "Experience the laid-back nightlife of Weligama with beach bars and live music.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Weligama
for activity in weligama_activities_data:
    Activity.objects.create(
        location=weligama,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Beruwala Location (Checking if already exists)
beruwala, created = Location.objects.get_or_create(
    name="Beruwala",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Beruwala",
        "notes": "Beruwala is a popular coastal town known for its beaches and historical significance."
    }
)

# Activity data for Beruwala with varying prices and categories
beruwala_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Beruwala Mosque", "category": "Cultural and Heritage Tours", "price": 10, "description": "Visit the historic Beruwala Mosque, one of the oldest mosques in Sri Lanka.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit Kande Vihara Temple", "category": "Cultural and Heritage Tours", "price": 12, "description": "Explore the Kande Vihara Temple, a major Buddhist site in Beruwala.", "price_range": "Low", "activity_rank": 2},
    {"name": "Explore Galle Fort", "category": "Cultural and Heritage Tours", "price": 15, "description": "A short trip to Galle Fort, a UNESCO World Heritage site with colonial architecture.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Stilt Fishing in Beruwala", "category": "Cultural and Heritage Tours", "price": 20, "description": "Experience the traditional stilt fishing technique practiced by the local fishermen.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Heritage Walk in Beruwala", "category": "Cultural and Heritage Tours", "price": 18, "description": "A heritage walk through Beruwala, exploring the local culture and landmarks.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Whale Watching from Beruwala", "category": "Nature and Wildlife Tours", "price": 50, "description": "Go whale watching along the coast of Beruwala, a prime whale watching destination.", "price_range": "High", "activity_rank": 1},
    {"name": "Mangrove Tour in Beruwala", "category": "Nature and Wildlife Tours", "price": 20, "description": "Take a boat ride through the Beruwala mangroves to discover its unique ecosystem.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Visit Brief Garden", "category": "Nature and Wildlife Tours", "price": 15, "description": "Explore Brief Garden, a beautiful tropical garden in Beruwala.", "price_range": "Low", "activity_rank": 3},
    {"name": "Turtle Watching in Beruwala", "category": "Nature and Wildlife Tours", "price": 25, "description": "Observe sea turtles nesting on Beruwala's coastline.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Bird Watching Tour", "category": "Nature and Wildlife Tours", "price": 30, "description": "Discover the diverse bird species in Beruwala’s natural reserves.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Beruwala Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Enjoy the peaceful, unspoiled beaches of Beruwala.", "price_range": "Low", "activity_rank": 1},
    {"name": "Surfing in Beruwala", "category": "Beach and Coastal Tours", "price": 20, "description": "Experience surfing at Beruwala's beach, known for its surf-friendly waves.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Sunset at Beruwala Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Watch a stunning sunset over the Indian Ocean from Beruwala beach.", "price_range": "Low", "activity_rank": 3},
    {"name": "Diving at Beruwala", "category": "Beach and Coastal Tours", "price": 35, "description": "Explore the coral reefs and underwater life through diving in Beruwala.", "price_range": "High", "activity_rank": 4},
    {"name": "Fishing Trip in Beruwala", "category": "Beach and Coastal Tours", "price": 25, "description": "Go on a traditional fishing trip off the coast of Beruwala.", "price_range": "Medium", "activity_rank": 5},

    # Adventure Tours
    {"name": "Jet Skiing in Beruwala", "category": "Adventure Tours", "price": 30, "description": "Enjoy an adrenaline-filled jet ski experience on the Beruwala coast.", "price_range": "High", "activity_rank": 1},
    {"name": "Kayaking in Beruwala", "category": "Adventure Tours", "price": 20, "description": "Kayak along the tranquil waters of Beruwala.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Ziplining in Beruwala", "category": "Adventure Tours", "price": 35, "description": "Experience the thrill of ziplining over Beruwala's scenic landscape.", "price_range": "High", "activity_rank": 3},
    {"name": "Trekking to Beruwala Hill", "category": "Adventure Tours", "price": 12, "description": "Trek to the top of Beruwala Hill for panoramic views of the coastline.", "price_range": "Low", "activity_rank": 4},
    {"name": "Stand-Up Paddleboarding in Beruwala", "category": "Adventure Tours", "price": 18, "description": "Learn the art of paddleboarding on the calm waters of Beruwala beach.", "price_range": "Medium", "activity_rank": 5},

    # General Activities
    {"name": "Visit Beruwala Local Market", "category": "General", "price": 8, "description": "Explore the local market in Beruwala and sample fresh produce.", "price_range": "Low", "activity_rank": 1},
    {"name": "Cultural Evening in Beruwala", "category": "General", "price": 15, "description": "Enjoy an evening of traditional music and dance in Beruwala.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Yoga Retreat in Beruwala", "category": "General", "price": 25, "description": "Relax at a yoga retreat nestled in Beruwala’s natural beauty.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Seafood Feast in Beruwala", "category": "General", "price": 30, "description": "Indulge in a delicious seafood feast at one of Beruwala's finest restaurants.", "price_range": "High", "activity_rank": 4},
    {"name": "Nightlife in Beruwala", "category": "General", "price": 10, "description": "Experience the peaceful nightlife of Beruwala with local beachside bars.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Beruwala
for activity in beruwala_activities_data:
    Activity.objects.create(
        location=beruwala,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )




# dambulla kurunagala

from itinerary.models import Location, Activity

# Dambulla Location (Checking if already exists)
dambulla, created = Location.objects.get_or_create(
    name="Dambulla",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Dambulla",
        "notes": "Dambulla is known for its ancient rock temples and historical significance."
    }
)

# Activity data for Dambulla with varying prices and categories
dambulla_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Dambulla Cave Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the UNESCO World Heritage site featuring ancient cave temples.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit Golden Temple", "category": "Cultural and Heritage Tours", "price": 12, "description": "A visit to the Golden Temple, an iconic site in Dambulla with impressive sculptures.", "price_range": "Low", "activity_rank": 2},
    {"name": "Explore Sigiriya Rock Fortress", "category": "Cultural and Heritage Tours", "price": 15, "description": "Climb the Sigiriya Rock Fortress, a historic landmark nearby.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit Ancient Dambulla Temples", "category": "Cultural and Heritage Tours", "price": 14, "description": "Tour the ancient Dambulla temples, famous for their murals and sculptures.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Cultural Tour of Dambulla", "category": "Cultural and Heritage Tours", "price": 18, "description": "A guided cultural tour exploring Dambulla’s temples and history.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit Minneriya National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Explore Minneriya National Park, known for its wild elephants.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Safari at Kaudulla National Park", "category": "Nature and Wildlife Tours", "price": 30, "description": "Enjoy a wildlife safari at Kaudulla, famous for its elephants and bird species.", "price_range": "High", "activity_rank": 2},
    {"name": "Bird Watching at Dambulla", "category": "Nature and Wildlife Tours", "price": 15, "description": "Observe diverse bird species in Dambulla’s natural surroundings.", "price_range": "Low", "activity_rank": 3},
    {"name": "Trekking to Pidurangala Rock", "category": "Nature and Wildlife Tours", "price": 10, "description": "Hike to Pidurangala Rock for breathtaking views of Sigiriya.", "price_range": "Low", "activity_rank": 4},
    {"name": "Botanical Garden Visit", "category": "Nature and Wildlife Tours", "price": 20, "description": "Tour the local botanical gardens, home to unique plants and flowers.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours (Nearby Areas)
    {"name": "Relax at Anuradhapura Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Enjoy a peaceful day at the tranquil beaches near Dambulla.", "price_range": "Low", "activity_rank": 1},
    {"name": "Snorkeling in Habarana", "category": "Beach and Coastal Tours", "price": 20, "description": "Snorkel in the crystal-clear waters around Habarana, a short drive from Dambulla.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Sunset in Dambulla", "category": "Beach and Coastal Tours", "price": 8, "description": "Enjoy a beautiful sunset over Dambulla’s serene landscape.", "price_range": "Low", "activity_rank": 3},
    {"name": "Scuba Diving at Passikudah", "category": "Beach and Coastal Tours", "price": 35, "description": "Take a scuba diving trip to the beautiful underwater sites near Passikudah.", "price_range": "High", "activity_rank": 4},
    {"name": "Beach Picnic in Dambulla", "category": "Beach and Coastal Tours", "price": 10, "description": "Have a relaxing beach picnic with the local produce and scenic views.", "price_range": "Low", "activity_rank": 5},

    # Adventure Tours
    {"name": "Rock Climbing in Sigiriya", "category": "Adventure Tours", "price": 25, "description": "Try rock climbing at Sigiriya, known for its challenging but rewarding climb.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Kayaking in Minneriya", "category": "Adventure Tours", "price": 15, "description": "Enjoy kayaking in the calm waters of Minneriya Lake.", "price_range": "Low", "activity_rank": 2},
    {"name": "Trekking to Dambulla Cave", "category": "Adventure Tours", "price": 12, "description": "Hike up to the Dambulla Cave temples for a panoramic view of the surroundings.", "price_range": "Low", "activity_rank": 3},
    {"name": "Jeep Safari at Kaudulla National Park", "category": "Adventure Tours", "price": 35, "description": "Embark on an exciting jeep safari in Kaudulla National Park.", "price_range": "High", "activity_rank": 4},
    {"name": "Ziplining at Sigiriya", "category": "Adventure Tours", "price": 40, "description": "Experience the thrill of ziplining over Sigiriya Rock.", "price_range": "High", "activity_rank": 5},

    # General Activities
    {"name": "Cultural Show in Dambulla", "category": "General", "price": 10, "description": "Attend a traditional cultural show with music and dance.", "price_range": "Low", "activity_rank": 1},
    {"name": "Cycling Tour of Dambulla", "category": "General", "price": 12, "description": "Explore Dambulla by bike, visiting key cultural and scenic spots.", "price_range": "Low", "activity_rank": 2},
    {"name": "Yoga Retreat in Dambulla", "category": "General", "price": 20, "description": "Relax and rejuvenate with a yoga retreat surrounded by nature.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Local Cuisine Experience", "category": "General", "price": 15, "description": "Taste the local Sri Lankan cuisine in a cozy restaurant in Dambulla.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Night Safari in Dambulla", "category": "General", "price": 18, "description": "Take a guided night safari to explore the wildlife after dark.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Dambulla
for activity in dambulla_activities_data:
    Activity.objects.create(
        location=dambulla,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Kurunegala Location (Checking if already exists)
kurunegala, created = Location.objects.get_or_create(
    name="Kurunegala",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Kurunegala",
        "notes": "Kurunegala is known for its cultural heritage, historical sites, and scenic surroundings."
    }
)

# Activity data for Kurunegala with varying prices and categories
kurunegala_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Kurunegala Rock Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the ancient rock temple in Kurunegala with historical significance.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Ancient Royal Palace", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the ruins of the ancient royal palace in Kurunegala.", "price_range": "Low", "activity_rank": 2},
    {"name": "Explore the Kurunegala Town", "category": "Cultural and Heritage Tours", "price": 15, "description": "Tour the historical town of Kurunegala, rich with culture and heritage.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Wewala Reservoir", "category": "Cultural and Heritage Tours", "price": 14, "description": "Visit the ancient Wewala Reservoir, a historical water reservoir.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Kurunegala Historical Walk", "category": "Cultural and Heritage Tours", "price": 18, "description": "A historical walk exploring Kurunegala’s landmarks and cultural sites.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Nature Walk in Kurunegala", "category": "Nature and Wildlife Tours", "price": 12, "description": "A guided nature walk exploring Kurunegala's lush landscapes.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit to the Kurunegala Lake", "category": "Nature and Wildlife Tours", "price": 15, "description": "Enjoy a peaceful boat ride in Kurunegala Lake, surrounded by nature.", "price_range": "Low", "activity_rank": 2},
    {"name": "Wildlife Safari at Kurunegala", "category": "Nature and Wildlife Tours", "price": 20, "description": "Go on a wildlife safari to explore the rich biodiversity around Kurunegala.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Trekking to the Kurunegala Hill", "category": "Nature and Wildlife Tours", "price": 18, "description": "Hike to the Kurunegala Hill for scenic views of the surrounding area.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Bird Watching at Kurunegala", "category": "Nature and Wildlife Tours", "price": 10, "description": "Observe various bird species in Kurunegala's natural reserves.", "price_range": "Low", "activity_rank": 5},

    # Beach and Coastal Tours (Nearby Areas)
    {"name": "Relax at Marawila Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Enjoy the peaceful, uncrowded Marawila Beach, just a short drive from Kurunegala.", "price_range": "Low", "activity_rank": 1},
    {"name": "Surfing at Wadduwa Beach", "category": "Beach and Coastal Tours", "price": 20, "description": "Experience the surf-friendly waves of Wadduwa Beach.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Diving at Kalpitiya", "category": "Beach and Coastal Tours", "price": 35, "description": "Take a diving trip to Kalpitiya, known for its rich marine life.", "price_range": "High", "activity_rank": 3},
    {"name": "Fishing at Moratuwa", "category": "Beach and Coastal Tours", "price": 25, "description": "Go fishing along the coast of Moratuwa, near Kurunegala.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Sunset at Hikkaduwa Beach", "category": "Beach and Coastal Tours", "price": 10, "description": "Watch a beautiful sunset at Hikkaduwa Beach, just a few hours away from Kurunegala.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Kurunegala
for activity in kurunegala_activities_data:
    Activity.objects.create(
        location=kurunegala,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# polonnaruwa badulla
from itinerary.models import Location, Activity

# Polonnaruwa Location (Checking if already exists)
polonnaruwa, created = Location.objects.get_or_create(
    name="Polonnaruwa",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Polonnaruwa",
        "notes": "Polonnaruwa is an ancient city and UNESCO World Heritage site, known for its well-preserved ruins and temples."
    }
)

# Activity data for Polonnaruwa with varying prices and categories
polonnaruwa_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Polonnaruwa Ruins", "category": "Cultural and Heritage Tours", "price": 12, "description": "Explore the ruins of Polonnaruwa, an ancient city with temples, sculptures, and historical significance.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit Gal Vihara", "category": "Cultural and Heritage Tours", "price": 15, "description": "Discover the ancient stone carvings and sculptures at Gal Vihara in Polonnaruwa.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Visit the Royal Palace Complex", "category": "Cultural and Heritage Tours", "price": 18, "description": "Tour the ruins of the Royal Palace, a majestic historical site in Polonnaruwa.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Explore the Lotus Pond", "category": "Cultural and Heritage Tours", "price": 10, "description": "Visit the ancient Lotus Pond, a beautiful historical feature in Polonnaruwa.", "price_range": "Low", "activity_rank": 4},
    {"name": "Visit Parakrama Samudra", "category": "Cultural and Heritage Tours", "price": 20, "description": "Explore the historic Parakrama Samudra, a massive ancient reservoir.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Safari at Minneriya National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Go on a wildlife safari in Minneriya National Park, famous for its elephant gatherings.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Visit the Polonnaruwa Nature Reserve", "category": "Nature and Wildlife Tours", "price": 15, "description": "Explore the natural beauty and wildlife of the Polonnaruwa Nature Reserve.", "price_range": "Low", "activity_rank": 2},
    {"name": "Bird Watching in Polonnaruwa", "category": "Nature and Wildlife Tours", "price": 10, "description": "Enjoy bird watching in the lush forests surrounding Polonnaruwa.", "price_range": "Low", "activity_rank": 3},
    {"name": "Boat Ride in Parakrama Samudra", "category": "Nature and Wildlife Tours", "price": 18, "description": "Take a peaceful boat ride on the Parakrama Samudra reservoir.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Nature Walk at Wasgamuwa National Park", "category": "Nature and Wildlife Tours", "price": 20, "description": "Hike through the Wasgamuwa National Park, famous for its wildlife and nature trails.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours (Nearby Areas)
    {"name": "Relax at Polonnaruwa Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Enjoy the calm and serene beaches near Polonnaruwa.", "price_range": "Low", "activity_rank": 1},
    {"name": "Snorkeling at Passikudah", "category": "Beach and Coastal Tours", "price": 20, "description": "Snorkel in the crystal-clear waters of Passikudah Beach, close to Polonnaruwa.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Scuba Diving at Kalkudah", "category": "Beach and Coastal Tours", "price": 35, "description": "Take a scuba diving trip in Kalkudah to explore vibrant marine life.", "price_range": "High", "activity_rank": 3},
    {"name": "Surfing at Nilaveli Beach", "category": "Beach and Coastal Tours", "price": 25, "description": "Experience the thrill of surfing in the beautiful Nilaveli Beach.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Fishing at Trincomalee", "category": "Beach and Coastal Tours", "price": 15, "description": "Try fishing at the peaceful shores of Trincomalee, near Polonnaruwa.", "price_range": "Low", "activity_rank": 5},

    # Adventure Tours
    {"name": "Rock Climbing in Sigiriya", "category": "Adventure Tours", "price": 25, "description": "Climb the famous Sigiriya Rock Fortress, an exhilarating adventure with stunning views.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Jeep Safari at Wasgamuwa National Park", "category": "Adventure Tours", "price": 30, "description": "Go on a jeep safari in Wasgamuwa National Park, perfect for spotting wildlife.", "price_range": "High", "activity_rank": 2},
    {"name": "Trekking in Polonnaruwa", "category": "Adventure Tours", "price": 12, "description": "Take a trekking tour in the Polonnaruwa area, ideal for adventure seekers.", "price_range": "Low", "activity_rank": 3},
    {"name": "Kayaking at Wasgamuwa Lake", "category": "Adventure Tours", "price": 15, "description": "Enjoy a kayaking experience at Wasgamuwa Lake, surrounded by wildlife.", "price_range": "Low", "activity_rank": 4},
    {"name": "Ziplining in Sigiriya", "category": "Adventure Tours", "price": 40, "description": "Experience the thrill of ziplining over Sigiriya Rock, a truly unique adventure.", "price_range": "High", "activity_rank": 5},

    # General Activities
    {"name": "Cultural Show in Polonnaruwa", "category": "General", "price": 10, "description": "Attend a cultural show featuring traditional Sri Lankan music and dance.", "price_range": "Low", "activity_rank": 1},
    {"name": "Cycling Tour around Polonnaruwa", "category": "General", "price": 12, "description": "Explore Polonnaruwa on a cycling tour, visiting key cultural and scenic spots.", "price_range": "Low", "activity_rank": 2},
    {"name": "Yoga Retreat in Polonnaruwa", "category": "General", "price": 18, "description": "Relax and rejuvenate with a yoga retreat surrounded by nature in Polonnaruwa.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Local Cuisine Experience", "category": "General", "price": 15, "description": "Taste the traditional Sri Lankan cuisine in a local Polonnaruwa restaurant.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Night Safari at Wasgamuwa", "category": "General", "price": 20, "description": "Experience a thrilling night safari in the Wasgamuwa National Park.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Polonnaruwa
for activity in polonnaruwa_activities_data:
    Activity.objects.create(
        location=polonnaruwa,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Badulla Location (Checking if already exists)
badulla, created = Location.objects.get_or_create(
    name="Badulla",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Badulla",
        "notes": "Badulla is a scenic town located in the Uva Province, known for its beautiful surroundings and cool climate."
    }
)

# Activity data for Badulla with varying prices and categories
badulla_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Badulla Buddhist Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the Badulla Buddhist Temple, rich in history and spiritual significance.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit Muthiyangana Raja Maha Vihara", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the historic Muthiyangana Raja Maha Vihara, an important Buddhist temple in Badulla.", "price_range": "Low", "activity_rank": 2},
    {"name": "Tour of Badulla Ancient Ruins", "category": "Cultural and Heritage Tours", "price": 18, "description": "Take a guided tour of the ancient ruins in Badulla, including historical temples and shrines.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Explore Dhowa Rock Temple", "category": "Cultural and Heritage Tours", "price": 20, "description": "Visit Dhowa Rock Temple, a famous ancient rock temple in Badulla.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Badulla Clock Tower", "category": "Cultural and Heritage Tours", "price": 15, "description": "Visit the iconic Badulla Clock Tower, a symbol of the town's history.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit Horton Plains National Park", "category": "Nature and Wildlife Tours", "price": 20, "description": "Explore Horton Plains National Park, famous for its stunning landscapes and biodiversity.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Hike to Ravana Falls", "category": "Nature and Wildlife Tours", "price": 12, "description": "Hike to Ravana Falls, a scenic and popular waterfall near Badulla.", "price_range": "Low", "activity_rank": 2},
    {"name": "Bird Watching at Ella Rock", "category": "Nature and Wildlife Tours", "price": 15, "description": "Enjoy bird watching at Ella Rock, home to diverse species of birds.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Safari in Udawalawe National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Go on a safari in Udawalawe National Park, known for its elephant population.", "price_range": "High", "activity_rank": 4},
    {"name": "Trekking in Badulla Hills", "category": "Nature and Wildlife Tours", "price": 18, "description": "Trek the scenic hills around Badulla for breathtaking views.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours (Nearby Areas)
    {"name": "Relax at Arugam Bay", "category": "Beach and Coastal Tours", "price": 5, "description": "Relax on the beautiful and serene Arugam Bay, a short trip from Badulla.", "price_range": "Low", "activity_rank": 1},
    {"name": "Surfing at Arugam Bay", "category": "Beach and Coastal Tours", "price": 20, "description": "Surf the famous waves of Arugam Bay, a popular destination for surfers.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Snorkeling at Nilaveli", "category": "Beach and Coastal Tours", "price": 25, "description": "Enjoy snorkeling at Nilaveli Beach, renowned for its rich marine life.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Fishing at Kirinda Beach", "category": "Beach and Coastal Tours", "price": 15, "description": "Try your hand at fishing on the tranquil Kirinda Beach.", "price_range": "Low", "activity_rank": 4},
    {"name": "Sunset at Tangalle Beach", "category": "Beach and Coastal Tours", "price": 10, "description": "Watch a stunning sunset at Tangalle Beach, close to Badulla.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Badulla
for activity in badulla_activities_data:
    Activity.objects.create(
        location=badulla,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )




# kegalle rathnapura mannar
from itinerary.models import Location, Activity

# Kegalle Location (Checking if already exists)
kegalle, created = Location.objects.get_or_create(
    name="Kegalle",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Kegalle",
        "notes": "Kegalle is known for its picturesque scenery and is a gateway to the beautiful Sabaragamuwa Province."
    }
)

# Activity data for Kegalle with varying prices and categories
kegalle_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Kegalle Museum", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the Kegalle Museum, showcasing the rich cultural history of the region.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Pinnawala Elephant Orphanage", "category": "Cultural and Heritage Tours", "price": 15, "description": "Visit the Pinnawala Elephant Orphanage and get a close look at Sri Lankan elephants.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Explore the Bopath Ella Waterfall", "category": "Cultural and Heritage Tours", "price": 20, "description": "Discover the stunning Bopath Ella Waterfall, a serene and scenic spot near Kegalle.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Doluwa Temple", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the Doluwa Temple, a historical and religious site in Kegalle.", "price_range": "Low", "activity_rank": 4},
    {"name": "Tour the Historical Sites of Kegalle", "category": "Cultural and Heritage Tours", "price": 18, "description": "Take a cultural tour through Kegalle, exploring the temples and other historical sites.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Safari at Udawalawe National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Go on a safari in Udawalawe National Park, a sanctuary for elephants and other wildlife.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Trekking in the Kegalle Hills", "category": "Nature and Wildlife Tours", "price": 15, "description": "Hike through the Kegalle Hills, enjoying the scenic views and lush greenery.", "price_range": "Low", "activity_rank": 2},
    {"name": "Bird Watching at Kegalle Wetlands", "category": "Nature and Wildlife Tours", "price": 10, "description": "Enjoy bird watching in the Kegalle Wetlands, home to many species of birds.", "price_range": "Low", "activity_rank": 3},
    {"name": "Nature Walk in Kegalle Forest", "category": "Nature and Wildlife Tours", "price": 20, "description": "Embark on a nature walk through Kegalle's forested areas, known for their biodiversity.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Kegalle Botanical Garden", "category": "Nature and Wildlife Tours", "price": 12, "description": "Explore the Kegalle Botanical Garden, showcasing the region's flora and plant life.", "price_range": "Low", "activity_rank": 5},

    # Beach and Coastal Tours (Nearby Areas)
    {"name": "Relax at Beruwala Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Relax at Beruwala Beach, a peaceful destination for sunbathing and swimming.", "price_range": "Low", "activity_rank": 1},
    {"name": "Snorkeling at Hikkaduwa Beach", "category": "Beach and Coastal Tours", "price": 20, "description": "Explore the underwater world with a snorkeling trip at Hikkaduwa Beach.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Surfing at Mirissa Beach", "category": "Beach and Coastal Tours", "price": 25, "description": "Try surfing at the popular Mirissa Beach, famous for its waves.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Fishing at Negombo Beach", "category": "Beach and Coastal Tours", "price": 15, "description": "Join a fishing tour at Negombo Beach, a traditional coastal activity.", "price_range": "Low", "activity_rank": 4},
    {"name": "Boat Ride at Kalpitiya", "category": "Beach and Coastal Tours", "price": 18, "description": "Enjoy a boat ride at Kalpitiya, an area known for its marine biodiversity.", "price_range": "Medium", "activity_rank": 5},

    # Adventure Tours
    {"name": "Hiking to Adam's Peak", "category": "Adventure Tours", "price": 30, "description": "Hike up the sacred Adam's Peak, one of Sri Lanka's most iconic and challenging treks.", "price_range": "High", "activity_rank": 1},
    {"name": "Jeep Safari in Wilpattu National Park", "category": "Adventure Tours", "price": 25, "description": "Embark on an exciting jeep safari in Wilpattu National Park to see wildlife in their natural habitat.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Ziplining in Kegalle", "category": "Adventure Tours", "price": 15, "description": "Experience the thrill of ziplining through the Kegalle forests, a thrilling adventure.", "price_range": "Low", "activity_rank": 3},
    {"name": "Caving at Bopath Ella Cave", "category": "Adventure Tours", "price": 20, "description": "Explore the Bopath Ella Cave, a hidden gem with a touch of adventure.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Cycling Tour of Kegalle", "category": "Adventure Tours", "price": 18, "description": "Take a cycling tour through the beautiful landscapes of Kegalle.", "price_range": "Medium", "activity_rank": 5},

    # General Activities
    {"name": "Local Cuisine Tour", "category": "General", "price": 12, "description": "Taste local delicacies in Kegalle with a guided food tour.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Kegalle Tea Factory", "category": "General", "price": 15, "description": "Tour the Kegalle Tea Factory and learn how Sri Lankan tea is produced.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Yoga at Kegalle Wellness Center", "category": "General", "price": 18, "description": "Join a yoga session at the Kegalle Wellness Center for relaxation and health.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Cultural Dance Performance", "category": "General", "price": 10, "description": "Watch a traditional Sri Lankan cultural dance performance in Kegalle.", "price_range": "Low", "activity_rank": 4},
    {"name": "Photography Tour in Kegalle", "category": "General", "price": 15, "description": "Join a photography tour and capture the natural beauty of Kegalle.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Kegalle
for activity in kegalle_activities_data:
    Activity.objects.create(
        location=kegalle,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Ratnapura Location (Checking if already exists)
ratnapura, created = Location.objects.get_or_create(
    name="Ratnapura",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Ratnapura",
        "notes": "Ratnapura is known as the city of gems, located in the Sabaragamuwa Province of Sri Lanka."
    }
)

# Activity data for Ratnapura with varying prices and categories
ratnapura_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Ratnapura Gem Museum", "category": "Cultural and Heritage Tours", "price": 12, "description": "Discover the rich history of gems in Sri Lanka at the Ratnapura Gem Museum.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Sri Sumanaramaya Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Visit the Sri Sumanaramaya Temple, an important Buddhist temple in Ratnapura.", "price_range": "Low", "activity_rank": 2},
    {"name": "Explore the Ratnapura Historical Sites", "category": "Cultural and Heritage Tours", "price": 15, "description": "Tour the historical landmarks in Ratnapura, known for its colonial-era architecture.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Tour the Godagala Temple", "category": "Cultural and Heritage Tours", "price": 20, "description": "Visit the Godagala Temple, a revered site in Ratnapura with stunning views.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Ratnapura Clock Tower", "category": "Cultural and Heritage Tours", "price": 8, "description": "See the iconic Ratnapura Clock Tower, a landmark of the city.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Hike to Adam's Peak", "category": "Nature and Wildlife Tours", "price": 30, "description": "Climb the famous Adam's Peak, a sacred mountain with stunning views.", "price_range": "High", "activity_rank": 1},
    {"name": "Bird Watching at Sinharaja Forest Reserve", "category": "Nature and Wildlife Tours", "price": 15, "description": "Explore the UNESCO-listed Sinharaja Forest Reserve, known for its biodiversity.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Visit Udawalawe National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Embark on a safari in Udawalawe National Park to see elephants and other wildlife.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Ratnapura Waterfalls", "category": "Nature and Wildlife Tours", "price": 18, "description": "See the scenic waterfalls in the Ratnapura region.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Explore the Ratnapura Rainforest", "category": "Nature and Wildlife Tours", "price": 20, "description": "Take a guided tour through the rainforest in Ratnapura, rich in biodiversity.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours (Nearby Areas)
    {"name": "Relax at Beruwala Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Relax at Beruwala Beach, a peaceful destination for sunbathing and swimming.", "price_range": "Low", "activity_rank": 1},
    {"name": "Snorkeling at Hikkaduwa Beach", "category": "Beach and Coastal Tours", "price": 20, "description": "Explore the underwater world with a snorkeling trip at Hikkaduwa Beach.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Surfing at Mirissa Beach", "category": "Beach and Coastal Tours", "price": 25, "description": "Try surfing at the popular Mirissa Beach, famous for its waves.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Fishing at Negombo Beach", "category": "Beach and Coastal Tours", "price": 15, "description": "Join a fishing tour at Negombo Beach, a traditional coastal activity.", "price_range": "Low", "activity_rank": 4},
    {"name": "Boat Ride at Kalpitiya", "category": "Beach and Coastal Tours", "price": 18, "description": "Enjoy a boat ride at Kalpitiya, an area known for its marine biodiversity.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Ratnapura
for activity in ratnapura_activities_data:
    Activity.objects.create(
        location=ratnapura,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Mannar Location (Checking if already exists)
mannar, created = Location.objects.get_or_create(
    name="Mannar",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Mannar",
        "notes": "Mannar is a coastal city known for its natural beauty, including pristine beaches and the famous Mannar Island."
    }
)

# Activity data for Mannar with varying prices and categories
mannar_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Mannar Fort", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the historical Mannar Fort, a reminder of colonial history.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore the Kappaladi Buddhist Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the Kappaladi Buddhist Temple, an ancient site in Mannar.", "price_range": "Low", "activity_rank": 2},
    {"name": "Tour the Mannar Lighthouse", "category": "Cultural and Heritage Tours", "price": 15, "description": "Climb the Mannar Lighthouse for panoramic views of the area.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Giant's Tank", "category": "Cultural and Heritage Tours", "price": 18, "description": "Visit the historic Giant's Tank, an ancient irrigation reservoir in Mannar.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Explore the Mannar Ruins", "category": "Cultural and Heritage Tours", "price": 20, "description": "Explore the ruins of ancient structures, offering a glimpse into Mannar's rich history.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit the Mannar Bird Sanctuary", "category": "Nature and Wildlife Tours", "price": 12, "description": "Visit the Mannar Bird Sanctuary, home to many migratory birds.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore the Thaleimannar Beach", "category": "Nature and Wildlife Tours", "price": 8, "description": "Take a peaceful walk along Thaleimannar Beach, known for its natural beauty.", "price_range": "Low", "activity_rank": 2},
    {"name": "Snorkeling at Mannar Islands", "category": "Nature and Wildlife Tours", "price": 20, "description": "Explore the rich marine life around Mannar Islands with a snorkeling tour.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Go Whale Watching in Mannar", "category": "Nature and Wildlife Tours", "price": 30, "description": "Experience whale watching in Mannar, known for seasonal sightings of blue whales.", "price_range": "High", "activity_rank": 4},
    {"name": "Explore the Coral Reefs of Mannar", "category": "Nature and Wildlife Tours", "price": 25, "description": "Discover the coral reefs near Mannar, a haven for marine biodiversity.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at the Thaleimannar Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Enjoy the beautiful, serene Thaleimannar Beach.", "price_range": "Low", "activity_rank": 1},
    {"name": "Fishing at Mannar Islands", "category": "Beach and Coastal Tours", "price": 15, "description": "Try fishing at Mannar Islands, a peaceful and popular activity.", "price_range": "Low", "activity_rank": 2},
    {"name": "Sunset at Thaleimannar", "category": "Beach and Coastal Tours", "price": 10, "description": "Enjoy a stunning sunset at Thaleimannar Beach.", "price_range": "Low", "activity_rank": 3},
    {"name": "Visit the Arippu Beach", "category": "Beach and Coastal Tours", "price": 12, "description": "Visit Arippu Beach, a scenic and tranquil destination in Mannar.", "price_range": "Low", "activity_rank": 4},
    {"name": "Snorkeling at Mannar Islands", "category": "Beach and Coastal Tours", "price": 20, "description": "Experience the underwater beauty of Mannar Islands with a snorkeling tour.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Mannar
for activity in mannar_activities_data:
    Activity.objects.create(
        location=mannar,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )

print("Data for Kegalle, Ratnapura, and Mannar has been added successfully.")




# Hikkaduwa matara jaffna

from itinerary.models import Location, Activity

# Hikkaduwa Location (Checking if already exists)
hikkaduwa, created = Location.objects.get_or_create(
    name="Hikkaduwa",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Hikkaduwa",
        "notes": "Hikkaduwa is a coastal city known for its beautiful beaches, marine life, and water sports."
    }
)

# Activity data for Hikkaduwa with varying prices and categories
hikkaduwa_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Hikkaduwa Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the ancient Hikkaduwa Temple, a site of historical significance.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore the Hikkaduwa Historical Sites", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit historical landmarks and the colonial-era architecture in Hikkaduwa.", "price_range": "Low", "activity_rank": 2},
    {"name": "Tour the Hikkaduwa Fort", "category": "Cultural and Heritage Tours", "price": 18, "description": "Explore the Hikkaduwa Fort, built during the Dutch colonial period.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Tsunami Memorial", "category": "Cultural and Heritage Tours", "price": 10, "description": "Learn about the 2004 tsunami disaster at the Tsunami Memorial in Hikkaduwa.", "price_range": "Low", "activity_rank": 4},
    {"name": "Hikkaduwa Heritage Walk", "category": "Cultural and Heritage Tours", "price": 15, "description": "Take a guided heritage walk to explore the cultural richness of Hikkaduwa.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Snorkeling at Hikkaduwa Coral Reef", "category": "Nature and Wildlife Tours", "price": 20, "description": "Explore the underwater world at Hikkaduwa's coral reefs, home to vibrant marine life.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Visit the Hikkaduwa National Park", "category": "Nature and Wildlife Tours", "price": 15, "description": "Explore the diverse flora and fauna in the Hikkaduwa National Park.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Go Dolphin Watching at Hikkaduwa", "category": "Nature and Wildlife Tours", "price": 25, "description": "Join a boat tour to see dolphins in their natural habitat near Hikkaduwa.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit Hikkaduwa Lagoon", "category": "Nature and Wildlife Tours", "price": 15, "description": "Take a boat ride in Hikkaduwa Lagoon to experience its serene beauty and wildlife.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Explore Hikkaduwa's Mangrove Forest", "category": "Nature and Wildlife Tours", "price": 18, "description": "Discover the mangrove ecosystems near Hikkaduwa and the diverse wildlife that inhabits it.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Hikkaduwa Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Enjoy a relaxing day at Hikkaduwa Beach, famous for its clear waters and golden sand.", "price_range": "Low", "activity_rank": 1},
    {"name": "Surfing at Hikkaduwa Beach", "category": "Beach and Coastal Tours", "price": 20, "description": "Learn to surf or enjoy the waves at Hikkaduwa Beach, one of Sri Lanka’s top surfing spots.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Snorkeling at Hikkaduwa Reef", "category": "Beach and Coastal Tours", "price": 20, "description": "Experience underwater life at Hikkaduwa's coral reef with guided snorkeling tours.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Fishing at Hikkaduwa Beach", "category": "Beach and Coastal Tours", "price": 15, "description": "Join a local fisherman for a fishing expedition at Hikkaduwa Beach.", "price_range": "Low", "activity_rank": 4},
    {"name": "Sunset Boat Ride at Hikkaduwa", "category": "Beach and Coastal Tours", "price": 18, "description": "Take a scenic sunset boat ride along the coast of Hikkaduwa.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Hikkaduwa
for activity in hikkaduwa_activities_data:
    Activity.objects.create(
        location=hikkaduwa,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Matara Location (Checking if already exists)
matara, created = Location.objects.get_or_create(
    name="Matara",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Matara",
        "notes": "Matara is a coastal city known for its historical landmarks and beautiful beaches."
    }
)

# Activity data for Matara with varying prices and categories
matara_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Matara Fort", "category": "Cultural and Heritage Tours", "price": 12, "description": "Explore the historic Matara Fort, which dates back to the Dutch colonial era.", "price_range": "Low", "activity_rank": 1},
    {"name": "Tour the Weherahena Buddhist Temple", "category": "Cultural and Heritage Tours", "price": 15, "description": "Visit the Weherahena Buddhist Temple, known for its grand structure and religious significance.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Visit the Matara Clock Tower", "category": "Cultural and Heritage Tours", "price": 10, "description": "See the iconic Matara Clock Tower, a historical landmark in the city.", "price_range": "Low", "activity_rank": 3},
    {"name": "Explore the Matara City Museum", "category": "Cultural and Heritage Tours", "price": 8, "description": "Visit the Matara City Museum to learn about the cultural heritage of the region.", "price_range": "Low", "activity_rank": 4},
    {"name": "Visit the Old Dutch Church", "category": "Cultural and Heritage Tours", "price": 10, "description": "Tour the Old Dutch Church, a reminder of the colonial past in Matara.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit the Kalametiya Bird Sanctuary", "category": "Nature and Wildlife Tours", "price": 20, "description": "Explore the Kalametiya Bird Sanctuary, home to various bird species.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Safari at Yala National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Join a safari at Yala National Park to see leopards, elephants, and other wildlife.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Snorkeling at Polhena Beach", "category": "Nature and Wildlife Tours", "price": 15, "description": "Enjoy snorkeling at Polhena Beach, famous for its coral reefs and sea turtles.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Mulgirigala Rock Temple", "category": "Nature and Wildlife Tours", "price": 18, "description": "Explore the Mulgirigala Rock Temple, offering stunning views of the surrounding landscape.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Explore the Mirissa Whale Watching", "category": "Nature and Wildlife Tours", "price": 30, "description": "Embark on a whale-watching expedition from Mirissa, known for blue whale sightings.", "price_range": "High", "activity_rank": 5},
]

# Insert activities into the database for Matara
for activity in matara_activities_data:
    Activity.objects.create(
        location=matara,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Jaffna Location (Checking if already exists)
jaffna, created = Location.objects.get_or_create(
    name="Jaffna",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Jaffna",
        "notes": "Jaffna is a city known for its unique cultural heritage and beautiful landscapes."
    }
)

# Activity data for Jaffna with varying prices and categories
jaffna_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Jaffna Fort", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the historic Jaffna Fort, a reminder of the colonial past.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore the Nallur Kovil", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the sacred Nallur Kovil, an important Hindu temple in Jaffna.", "price_range": "Low", "activity_rank": 2},
    {"name": "Visit the Jaffna Archaeological Museum", "category": "Cultural and Heritage Tours", "price": 8, "description": "Discover the rich history of Jaffna at the Archaeological Museum.", "price_range": "Low", "activity_rank": 3},
    {"name": "Take a walk through Jaffna Market", "category": "Cultural and Heritage Tours", "price": 5, "description": "Visit the bustling Jaffna Market for local produce and cultural goods.", "price_range": "Low", "activity_rank": 4},
    {"name": "Jaffna Heritage Tour", "category": "Cultural and Heritage Tours", "price": 15, "description": "Take a guided heritage tour through the cultural heart of Jaffna.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit the Jaffna Lagoon", "category": "Nature and Wildlife Tours", "price": 12, "description": "Explore the scenic Jaffna Lagoon, a haven for birdwatchers and nature enthusiasts.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Casuarina Beach", "category": "Nature and Wildlife Tours", "price": 15, "description": "Relax at Casuarina Beach, one of Jaffna's most beautiful and tranquil spots.", "price_range": "Low", "activity_rank": 2},
    {"name": "Jaffna Bird Watching Tour", "category": "Nature and Wildlife Tours", "price": 20, "description": "Explore the rich birdlife of Jaffna on a guided bird-watching tour.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Explore the Delft Island", "category": "Nature and Wildlife Tours", "price": 25, "description": "Visit Delft Island for a peaceful retreat and the chance to see wild ponies.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Snorkeling at Neduntheevu", "category": "Nature and Wildlife Tours", "price": 30, "description": "Snorkel in the crystal-clear waters off Neduntheevu (Delft Island).", "price_range": "High", "activity_rank": 5},
]

# Insert activities into the database for Jaffna
for activity in jaffna_activities_data:
    Activity.objects.create(
        location=jaffna,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )

print("Data for Hikkaduwa, Matara, and Jaffna has been added successfully.")





# trinco ella sigiriya

from itinerary.models import Location, Activity

# Trincomalee Location (Checking if already exists)
trincomalee, created = Location.objects.get_or_create(
    name="Trincomalee",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Trincomalee",
        "notes": "Trincomalee is a coastal city known for its historical significance, beautiful beaches, and marine life."
    }
)

# Activity data for Trincomalee with varying prices and categories
trincomalee_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Trincomalee Fort", "category": "Cultural and Heritage Tours", "price": 12, "description": "Explore the historic Trincomalee Fort, a key site in Sri Lanka's colonial past.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Koneswaram Temple", "category": "Cultural and Heritage Tours", "price": 15, "description": "Discover the cultural and religious significance of the Koneswaram Temple.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Explore the Nilaveli Temple", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the ancient Nilaveli Temple, a hidden gem in Trincomalee.", "price_range": "Low", "activity_rank": 3},
    {"name": "Trincomalee City Tour", "category": "Cultural and Heritage Tours", "price": 18, "description": "Take a guided tour through Trincomalee, highlighting its historical landmarks.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Trincomalee Heritage Walk", "category": "Cultural and Heritage Tours", "price": 20, "description": "Take a walk through Trincomalee's colonial-era buildings and historical sites.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Snorkeling at Pigeon Island", "category": "Nature and Wildlife Tours", "price": 25, "description": "Snorkel at Pigeon Island National Park, one of Sri Lanka's most beautiful marine reserves.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Whale Watching in Trincomalee", "category": "Nature and Wildlife Tours", "price": 30, "description": "Join a whale watching tour to see blue whales, sperm whales, and dolphins.", "price_range": "High", "activity_rank": 2},
    {"name": "Visit the Trincomalee Hot Springs", "category": "Nature and Wildlife Tours", "price": 18, "description": "Relax in the natural hot springs found in Trincomalee, known for their therapeutic properties.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Explore the Trincomalee Coral Gardens", "category": "Nature and Wildlife Tours", "price": 20, "description": "Dive into the pristine coral gardens of Trincomalee, a haven for marine biodiversity.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Pigeon Island National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Take a boat ride and enjoy the natural beauty of Pigeon Island National Park.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Trincomalee Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Enjoy the serene and pristine beaches of Trincomalee, a perfect place for relaxation.", "price_range": "Low", "activity_rank": 1},
    {"name": "Snorkeling at Uppuveli Beach", "category": "Beach and Coastal Tours", "price": 18, "description": "Snorkel in the crystal-clear waters of Uppuveli Beach, known for its rich marine life.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Surfing at Nilaveli Beach", "category": "Beach and Coastal Tours", "price": 20, "description": "Learn to surf or enjoy the waves at Nilaveli Beach, one of Sri Lanka’s best surfing spots.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Trincomalee Boat Ride", "category": "Beach and Coastal Tours", "price": 15, "description": "Take a boat ride along the coastline of Trincomalee to enjoy its stunning views.", "price_range": "Low", "activity_rank": 4},
    {"name": "Sunset View at Trincomalee Beach", "category": "Beach and Coastal Tours", "price": 12, "description": "Enjoy the breathtaking sunset views from Trincomalee Beach.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Trincomalee
for activity in trincomalee_activities_data:
    Activity.objects.create(
        location=trincomalee,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Ella Location (Checking if already exists)
ella, created = Location.objects.get_or_create(
    name="Ella",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Ella",
        "notes": "Ella is a scenic hill town in Sri Lanka, famous for its waterfalls, trekking paths, and panoramic views."
    }
)

# Activity data for Ella with varying prices and categories
ella_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Ella Rock", "category": "Cultural and Heritage Tours", "price": 10, "description": "Trek to Ella Rock for panoramic views of the surrounding mountains and valley.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore the Ravana Temple", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the Ravana Temple, a site of religious significance and historical value.", "price_range": "Low", "activity_rank": 2},
    {"name": "Ella Heritage Walk", "category": "Cultural and Heritage Tours", "price": 15, "description": "Take a walk through the town of Ella, learning about its rich cultural history.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Nine Arches Bridge", "category": "Cultural and Heritage Tours", "price": 10, "description": "Visit the famous Nine Arches Bridge, an iconic architectural wonder in Ella.", "price_range": "Low", "activity_rank": 4},
    {"name": "Ella Historical Tour", "category": "Cultural and Heritage Tours", "price": 15, "description": "Join a historical tour that explores Ella's significance in Sri Lanka’s history.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit the Ravana Falls", "category": "Nature and Wildlife Tours", "price": 8, "description": "Explore the stunning Ravana Falls, one of Sri Lanka’s most famous waterfalls.", "price_range": "Low", "activity_rank": 1},
    {"name": "Ella Jungle Trek", "category": "Nature and Wildlife Tours", "price": 18, "description": "Take a guided jungle trek through Ella’s lush rainforest and spot native wildlife.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Explore the Diyaluma Falls", "category": "Nature and Wildlife Tours", "price": 15, "description": "Visit the beautiful Diyaluma Falls, one of the highest waterfalls in Sri Lanka.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Bird Watching at Ella", "category": "Nature and Wildlife Tours", "price": 20, "description": "Join a bird-watching tour to see Ella's rich biodiversity, including endemic species.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Ella Botanical Garden", "category": "Nature and Wildlife Tours", "price": 12, "description": "Take a stroll through the Ella Botanical Garden, known for its variety of plant species.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Ella
for activity in ella_activities_data:
    Activity.objects.create(
        location=ella,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Sigiriya Location (Checking if already exists)
sigiriya, created = Location.objects.get_or_create(
    name="Sigiriya",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Sigiriya",
        "notes": "Sigiriya is an ancient rock fortress, renowned for its frescoes, gardens, and archaeological significance."
    }
)

# Activity data for Sigiriya with varying prices and categories
sigiriya_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit Sigiriya Rock Fortress", "category": "Cultural and Heritage Tours", "price": 25, "description": "Climb the iconic Sigiriya Rock Fortress, a UNESCO World Heritage Site.", "price_range": "High", "activity_rank": 1},
    {"name": "Explore the Sigiriya Frescoes", "category": "Cultural and Heritage Tours", "price": 20, "description": "Admire the ancient frescoes that adorn the Sigiriya rock face.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Sigiriya Village Tour", "category": "Cultural and Heritage Tours", "price": 15, "description": "Experience the local culture with a village tour around Sigiriya.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Sigiriya Garden Walk", "category": "Cultural and Heritage Tours", "price": 10, "description": "Walk through the beautiful water gardens of Sigiriya, dating back to the 5th century.", "price_range": "Low", "activity_rank": 4},
    {"name": "Sigiriya History Tour", "category": "Cultural and Heritage Tours", "price": 18, "description": "Take a guided tour to learn about Sigiriya’s ancient history and archaeological importance.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit the Minneriya National Park", "category": "Nature and Wildlife Tours", "price": 20, "description": "Go on a safari at Minneriya National Park to see elephants and other wildlife.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Explore the Sigiriya Jungle", "category": "Nature and Wildlife Tours", "price": 18, "description": "Take a nature walk in the Sigiriya Jungle, home to various flora and fauna.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Elephant Safari at Habarana", "category": "Nature and Wildlife Tours", "price": 30, "description": "Join an elephant safari in Habarana, a nearby town famous for its wild elephant population.", "price_range": "High", "activity_rank": 3},
    {"name": "Bird Watching at Sigiriya", "category": "Nature and Wildlife Tours", "price": 12, "description": "Enjoy a peaceful bird-watching experience around the Sigiriya area.", "price_range": "Low", "activity_rank": 4},
    {"name": "Visit the Sigiriya Lake", "category": "Nature and Wildlife Tours", "price": 10, "description": "Explore the serene Sigiriya Lake, a picturesque spot surrounded by lush vegetation.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Sigiriya
for activity in sigiriya_activities_data:
    Activity.objects.create(
        location=sigiriya,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )

print("Data for Trincomalee, Ella, and Sigiriya has been added successfully.")




# anuradhapura negambo nuwara eliya

from itinerary.models import Location, Activity

# Anuradhapura Location (Checking if already exists)
anuradhapura, created = Location.objects.get_or_create(
    name="Anuradhapura",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Anuradhapura",
        "notes": "Anuradhapura is one of Sri Lanka's ancient capitals, famous for its sacred Buddhist sites and historical ruins."
    }
)

# Activity data for Anuradhapura with varying prices and categories
anuradhapura_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Sri Maha Bodhi Tree", "category": "Cultural and Heritage Tours", "price": 5, "description": "Visit the Sri Maha Bodhi Tree, a sacred Buddhist site in Anuradhapura.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore the Ruwanwelisaya Stupa", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the ancient Ruwanwelisaya Stupa, a key Buddhist monument.", "price_range": "Low", "activity_rank": 2},
    {"name": "Visit the Isurumuniya Vihara", "category": "Cultural and Heritage Tours", "price": 8, "description": "Discover the Isurumuniya Vihara, a Buddhist temple known for its rock carvings.", "price_range": "Low", "activity_rank": 3},
    {"name": "Anuradhapura Historical Tour", "category": "Cultural and Heritage Tours", "price": 15, "description": "Take a guided tour of Anuradhapura’s historical ruins and temples.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Mihintale Monastery Visit", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the Mihintale Monastery, the cradle of Sri Lankan Buddhism.", "price_range": "Medium", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit Wilpattu National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Go on a safari at Wilpattu National Park, Sri Lanka’s largest wildlife park.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Bird Watching at Kala Wewa", "category": "Nature and Wildlife Tours", "price": 18, "description": "Enjoy bird-watching at Kala Wewa, a renowned bird sanctuary near Anuradhapura.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Visit the Tissa Wewa Lake", "category": "Nature and Wildlife Tours", "price": 10, "description": "Relax and enjoy nature at the picturesque Tissa Wewa Lake.", "price_range": "Low", "activity_rank": 3},
    {"name": "Explore the Anuradhapura Forest Reserve", "category": "Nature and Wildlife Tours", "price": 20, "description": "Take a trek through the Anuradhapura Forest Reserve, home to many species of plants and animals.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Mihintale Nature Trails", "category": "Nature and Wildlife Tours", "price": 12, "description": "Hike the nature trails of Mihintale and explore its diverse flora and fauna.", "price_range": "Low", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Visit the North Coast Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Relax on the pristine beaches of Anuradhapura's north coast.", "price_range": "Low", "activity_rank": 1},
    {"name": "Anuradhapura Boat Ride", "category": "Beach and Coastal Tours", "price": 10, "description": "Take a boat ride on the Tissa Wewa Lake for a peaceful experience.", "price_range": "Low", "activity_rank": 2},
    {"name": "Visit the Kalpitiya Peninsula", "category": "Beach and Coastal Tours", "price": 15, "description": "Explore the Kalpitiya Peninsula, known for its sandy beaches and coastal beauty.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Snorkeling at Trincomalee Beach", "category": "Beach and Coastal Tours", "price": 20, "description": "Snorkel in the clear waters of Trincomalee Beach, a short drive from Anuradhapura.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Whale Watching at Kalpitiya", "category": "Beach and Coastal Tours", "price": 30, "description": "Take a whale watching tour at Kalpitiya, one of Sri Lanka’s top whale-watching spots.", "price_range": "High", "activity_rank": 5},
]

# Insert activities into the database for Anuradhapura
for activity in anuradhapura_activities_data:
    Activity.objects.create(
        location=anuradhapura,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Negombo Location (Checking if already exists)
negombo, created = Location.objects.get_or_create(
    name="Negombo",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Negombo",
        "notes": "Negombo is a coastal city near Colombo, known for its beaches, fishing villages, and colonial-era architecture."
    }
)

# Activity data for Negombo with varying prices and categories
negombo_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit St. Mary's Church", "category": "Cultural and Heritage Tours", "price": 5, "description": "Visit St. Mary's Church, a beautiful colonial-era church in Negombo.", "price_range": "Low", "activity_rank": 1},
    {"name": "Explore Negombo Dutch Fort", "category": "Cultural and Heritage Tours", "price": 8, "description": "Explore the remains of the Dutch Fort, a historical landmark in Negombo.", "price_range": "Low", "activity_rank": 2},
    {"name": "Visit the Angurukaramulla Temple", "category": "Cultural and Heritage Tours", "price": 7, "description": "Discover the Angurukaramulla Temple, known for its Buddhist murals and statues.", "price_range": "Low", "activity_rank": 3},
    {"name": "Negombo Historical Tour", "category": "Cultural and Heritage Tours", "price": 12, "description": "Join a guided tour of Negombo’s rich colonial past and historic sites.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Old Dutch Cemetery", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the Old Dutch Cemetery, a historic site in the heart of Negombo.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Boat Ride in Negombo Lagoon", "category": "Nature and Wildlife Tours", "price": 15, "description": "Take a boat ride through the Negombo Lagoon and spot local birdlife.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Visit the Muthurajawela Wetlands", "category": "Nature and Wildlife Tours", "price": 18, "description": "Explore the Muthurajawela Wetlands, a rich ecosystem teeming with wildlife.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Bird Watching at Negombo Lagoon", "category": "Nature and Wildlife Tours", "price": 12, "description": "Enjoy bird watching in the peaceful surroundings of Negombo Lagoon.", "price_range": "Low", "activity_rank": 3},
    {"name": "Explore the Negombo Beach", "category": "Nature and Wildlife Tours", "price": 8, "description": "Relax and unwind at the beautiful beaches of Negombo.", "price_range": "Low", "activity_rank": 4},
    {"name": "Fishing Tour in Negombo", "category": "Nature and Wildlife Tours", "price": 20, "description": "Experience a fishing tour in the coastal waters of Negombo, a fishing hub.", "price_range": "Medium", "activity_rank": 5},
]

# Insert activities into the database for Negombo
for activity in negombo_activities_data:
    Activity.objects.create(
        location=negombo,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Nuwara Eliya Location (Checking if already exists)
nuwara_eliya, created = Location.objects.get_or_create(
    name="Nuwara Eliya",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=NuwaraEliya",
        "notes": "Nuwara Eliya is a hill station known for its tea plantations, cool climate, and colonial charm."
    }
)

# Activity data for Nuwara Eliya with varying prices and categories
nuwara_eliya_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Nuwara Eliya Golf Course", "category": "Cultural and Heritage Tours", "price": 20, "description": "Explore the colonial-era Nuwara Eliya Golf Course.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Explore the Hakgala Botanical Garden", "category": "Cultural and Heritage Tours", "price": 10, "description": "Take a tour of the beautiful Hakgala Botanical Garden, a peaceful retreat.", "price_range": "Low", "activity_rank": 2},
    {"name": "Visit the Pedro Tea Estate", "category": "Cultural and Heritage Tours", "price": 12, "description": "Visit the Pedro Tea Estate and learn about the tea production process.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Nuwara Eliya Historical Tour", "category": "Cultural and Heritage Tours", "price": 18, "description": "Join a guided tour of Nuwara Eliya, learning about its colonial history.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Nuwara Eliya Post Office", "category": "Cultural and Heritage Tours", "price": 5, "description": "Visit the iconic Nuwara Eliya Post Office, a historic landmark.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Hike to World's End", "category": "Nature and Wildlife Tours", "price": 15, "description": "Take a hike to World's End, a dramatic cliff with breathtaking views.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Visit Horton Plains National Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Explore the beautiful Horton Plains National Park and its wildlife.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Visit the Sita Amman Temple", "category": "Nature and Wildlife Tours", "price": 12, "description": "Explore the Sita Amman Temple, surrounded by lush forests and tea plantations.", "price_range": "Low", "activity_rank": 3},
    {"name": "Bird Watching at Nuwara Eliya", "category": "Nature and Wildlife Tours", "price": 10, "description": "Enjoy bird watching in the cool climate of Nuwara Eliya.", "price_range": "Low", "activity_rank": 4},
    {"name": "Trekking at Adam's Peak", "category": "Nature and Wildlife Tours", "price": 30, "description": "Trek to the summit of Adam's Peak, a revered pilgrimage site.", "price_range": "High", "activity_rank": 5},
]

# Insert activities into the database for Nuwara Eliya
for activity in nuwara_eliya_activities_data:
    Activity.objects.create(
        location=nuwara_eliya,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )

print("Data for Anuradhapura, Negombo, and Nuwara Eliya has been added successfully.")





# kandy galle

from itinerary.models import Location, Activity

# Galle Location (Checking if already exists)
galle, created = Location.objects.get_or_create(
    name="Galle",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Galle",
        "notes": "Galle is a coastal city with a rich colonial history, known for its Dutch fort and scenic beaches."
    }
)

# Activity data for Galle with varying prices and categories
galle_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Explore the Galle Fort", "category": "Cultural and Heritage Tours", "price": 7, "description": "Discover the UNESCO-listed Galle Fort, a blend of European and Asian architecture.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the National Maritime Museum", "category": "Cultural and Heritage Tours", "price": 5, "description": "Explore the National Maritime Museum to learn about Sri Lanka’s maritime history.", "price_range": "Low", "activity_rank": 2},
    {"name": "Galle Dutch Reformed Church Visit", "category": "Cultural and Heritage Tours", "price": 4, "description": "Visit the Dutch Reformed Church, an architectural gem from the colonial era.", "price_range": "Low", "activity_rank": 3},
    {"name": "Galle Heritage Tour", "category": "Cultural and Heritage Tours", "price": 12, "description": "Join a guided heritage tour around the Galle Fort and nearby historical landmarks.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Galle Lighthouse", "category": "Cultural and Heritage Tours", "price": 6, "description": "Visit the Galle Lighthouse, one of the oldest lighthouses in Sri Lanka.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Visit Kanneliya Rainforest Reserve", "category": "Nature and Wildlife Tours", "price": 18, "description": "Explore the Kanneliya Rainforest Reserve, a biodiversity hotspot.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Snorkeling in Hikkaduwa Marine Park", "category": "Nature and Wildlife Tours", "price": 25, "description": "Enjoy snorkeling in the crystal-clear waters of Hikkaduwa Marine Park.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Galle Bay Dolphin Watching", "category": "Nature and Wildlife Tours", "price": 15, "description": "Go dolphin watching in Galle Bay, a popular spot for marine life.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Visit the Sinharaja Forest Reserve", "category": "Nature and Wildlife Tours", "price": 20, "description": "Take a nature walk through the Sinharaja Forest, a UNESCO World Heritage Site.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Explore Rumassala Hill", "category": "Nature and Wildlife Tours", "price": 10, "description": "Hike to the top of Rumassala Hill for scenic views of Galle and the ocean.", "price_range": "Low", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Relax at Unawatuna Beach", "category": "Beach and Coastal Tours", "price": 5, "description": "Unwind at Unawatuna Beach, a beautiful and popular spot for swimming and relaxation.", "price_range": "Low", "activity_rank": 1},
    {"name": "Visit the Jungle Beach", "category": "Beach and Coastal Tours", "price": 8, "description": "Visit Jungle Beach, a secluded and tranquil beach perfect for swimming and sunbathing.", "price_range": "Low", "activity_rank": 2},
    {"name": "Surfing in Midigama", "category": "Beach and Coastal Tours", "price": 20, "description": "Catch some waves at Midigama, one of the best surfing spots in Sri Lanka.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Whale Watching at Mirissa", "category": "Beach and Coastal Tours", "price": 25, "description": "Go whale watching in Mirissa, a popular spot for blue whale sightings.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Weligama Beach", "category": "Beach and Coastal Tours", "price": 10, "description": "Enjoy the beach atmosphere and take part in water sports at Weligama Beach.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Galle
for activity in galle_activities_data:
    Activity.objects.create(
        location=galle,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )


# Kandy Location (Checking if already exists)
kandy, created = Location.objects.get_or_create(
    name="Kandy",
    defaults={
        "image_url": "https://via.placeholder.com/150?text=Kandy",
        "notes": "Kandy is a scenic city located in the central highlands of Sri Lanka, known for its sacred temples and cultural heritage."
    }
)

# Activity data for Kandy with varying prices and categories
kandy_activities_data = [
    # Cultural and Heritage Tours
    {"name": "Visit the Temple of the Tooth", "category": "Cultural and Heritage Tours", "price": 10, "description": "Explore the Temple of the Tooth, one of the most sacred Buddhist sites in Sri Lanka.", "price_range": "Low", "activity_rank": 1},
    {"name": "Kandy Lake Tour", "category": "Cultural and Heritage Tours", "price": 8, "description": "Take a boat tour on Kandy Lake, a scenic spot surrounded by lush greenery.", "price_range": "Low", "activity_rank": 2},
    {"name": "Explore the Royal Botanical Gardens", "category": "Cultural and Heritage Tours", "price": 12, "description": "Wander through the Royal Botanical Gardens in Peradeniya, home to thousands of plant species.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Kandy Cultural Dance Show", "category": "Cultural and Heritage Tours", "price": 10, "description": "Watch a traditional Kandyan dance show, showcasing Sri Lanka’s vibrant culture.", "price_range": "Medium", "activity_rank": 4},
    {"name": "Visit the Kandy Museum", "category": "Cultural and Heritage Tours", "price": 7, "description": "Explore the Kandy Museum and discover the history of the city.", "price_range": "Low", "activity_rank": 5},

    # Nature and Wildlife Tours
    {"name": "Hike to Knuckles Mountain Range", "category": "Nature and Wildlife Tours", "price": 20, "description": "Go hiking in the Knuckles Mountain Range, a UNESCO World Heritage Site.", "price_range": "Medium", "activity_rank": 1},
    {"name": "Visit Udawatta Kele Sanctuary", "category": "Nature and Wildlife Tours", "price": 12, "description": "Explore the Udawatta Kele Sanctuary, a hidden forest reserve in Kandy.", "price_range": "Medium", "activity_rank": 2},
    {"name": "Botanical Gardens Tour", "category": "Nature and Wildlife Tours", "price": 15, "description": "Take a guided tour of the lush Royal Botanical Gardens in Peradeniya.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Bird Watching at Victoria Reservoir", "category": "Nature and Wildlife Tours", "price": 10, "description": "Enjoy bird watching around the picturesque Victoria Reservoir near Kandy.", "price_range": "Low", "activity_rank": 4},
    {"name": "Explore the Mahaweli River", "category": "Nature and Wildlife Tours", "price": 18, "description": "Take a scenic boat ride along the Mahaweli River and enjoy the surrounding nature.", "price_range": "Medium", "activity_rank": 5},

    # Beach and Coastal Tours
    {"name": "Visit the Kandy Lake", "category": "Beach and Coastal Tours", "price": 5, "description": "Relax around Kandy Lake, a peaceful location amidst the city.", "price_range": "Low", "activity_rank": 1},
    {"name": "Lake Viewpoint at Kandy", "category": "Beach and Coastal Tours", "price": 6, "description": "Enjoy the beautiful view of Kandy Lake from the lake's viewpoint.", "price_range": "Low", "activity_rank": 2},
    {"name": "Visit the Templers' Hill", "category": "Beach and Coastal Tours", "price": 10, "description": "Visit Templers' Hill for panoramic views of the city and the surrounding mountains.", "price_range": "Medium", "activity_rank": 3},
    {"name": "Kandy City View", "category": "Beach and Coastal Tours", "price": 8, "description": "Take a city tour to explore Kandy’s beautiful landscapes and panoramic views.", "price_range": "Low", "activity_rank": 4},
    {"name": "Explore the Peradeniya Railway Station", "category": "Beach and Coastal Tours", "price": 7, "description": "Explore the historic Peradeniya Railway Station, known for its colonial architecture.", "price_range": "Low", "activity_rank": 5},
]

# Insert activities into the database for Kandy
for activity in kandy_activities_data:
    Activity.objects.create(
        location=kandy,
        name=activity["name"],
        category=activity["category"],
        price=activity["price"],
        description=activity["description"],
        price_range=activity["price_range"],
        activity_rank=activity["activity_rank"],
        image_url="https://via.placeholder.com/150"
    )

print("Data for Galle and Kandy has been added successfully.")
