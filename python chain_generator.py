# 10-Day Chain Generator with Digit-wise Mapping

# Digit-wise mapping
mapping = {'0':'5','1':'6','2':'7','3':'8','4':'9','5':'0','6':'1','7':'2','8':'3','9':'4'}

def map_box(box):
    return ''.join([mapping[d] for d in box])

def last2(n):
    return str(n)[-2:]

def generate_boxes(a,b):
    diff = (a+10-b) if a<b else (a-b)
    base = 100 - diff + b
    boxes = [str(base + 19*i)[-2:] for i in range(4)]
    return boxes

def check_box_match(box, day_num):
    # check if box contains day_num or mapped box contains day_num
    day_str = str(day_num)
    return day_str in box or day_str in map_box(box)

# Input 10 days
days = []
for i in range(1,11):
    val = input(f"Enter Day {i} number: ").strip()
    while not val.isdigit():
        val = input(f"Invalid! Enter numeric Day {i} number: ").strip()
    days.append(int(val))

current_index = 0

print("\n--- Boxes for each pair ---")
for i in range(9):
    boxes = generate_boxes(days[i], days[i+1])
    print(f"Day {i+1}-{i+2} Boxes: {boxes}")
    
    found_index = -1
    for j, b in enumerate(boxes):
        if check_box_match(b, days[i+2]):
            found_index = j
            break
    
    if found_index>=0:
        print(f"Day {i+2} in these boxes: Box {found_index+1}")
        current_index = found_index
    else:
        print(f"Day {i+2} in these boxes: Not Found")

# Predict Day11 using last pair
last_boxes = generate_boxes(days[8], days[9])
predicted_box = last_boxes[current_index if current_index>=0 else 0]
print(f"\nPredicted Day11 Box: {predicted_box}")
