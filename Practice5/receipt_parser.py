import re
import json


text = "The rain in Spain"

# re.search() - finds the first match
match = re.search("ai", text)
print("search:", match.group() if match else "No match")

# re.findall() - finds all matches
found = re.findall("ai", text)
print("findall:", found)

# re.split() - splits string by pattern
split_result = re.split(r"\s", text)
print("split:", split_result)

# re.sub() - replaces matches
sub_result = re.sub(r"\s", "-", text)
print("sub:", sub_result)

# re.match() - checks only the beginning of the string
match_begin = re.match("The", text)
print("match:", match_begin.group() if match_begin else "No match")


#----------------------------------------------

sample = "abc 123 ABC"

print("digits:", re.findall(r"\d", sample))      # special sequence \d
print("word chars:", re.findall(r"\w", sample))  # special sequence \w
print("spaces:", re.findall(r"\s", sample))      # special sequence \s

print("starts with abc:", bool(re.search(r"^abc", sample)))  # ^
print("ends with ABC:", bool(re.search(r"ABC$", sample)))    # $
print("a followed by anything then c:", re.findall(r"a.*c", "abc axxxc"))

print("2 to 3 b's:", re.findall(r"ab{2,3}", "ab abb abbb abbbb"))




print("1:", re.findall(r"ab*", "a ab abb abbb ac"))
print("2:", re.findall(r"ab{2,3}", "ab abb abbb abbbb"))
print("3:", re.findall(r"\b[a-z]+_[a-z]+\b", "my_var test_value Hello"))
print("4:", re.findall(r"\b[A-Z][a-z]+\b", "Hello world Python is Fun"))
print("5:", re.findall(r"a.*b", "axxxb a123b ac"))
print("6:", re.sub(r"[ ,.]", ":", "Python, Java. C Sharp"))
print("7:", re.sub(r"_([a-z])", lambda m: m.group(1).upper(), "snake_case_string"))
print("8:", re.split(r"(?=[A-Z])", "SplitAtUpperCaseLetters"))
print("9:", re.sub(r"(?<!^)([A-Z])", r" \1", "InsertSpacesBetweenWords"))
print("10:", re.sub(r"([A-Z])", r"_\1", "CamelCaseString").lower().lstrip("_"))




with open("Practice5/raw.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

# 1. Extract all prices
# This finds numbers like 308,00 or 1 200,00
prices = re.findall(r"\d[\d ]*,\d{2}", raw_text)
print("All prices:", prices)

# 2. Extract product names
# Product name is usually between item number and quantity line
products = re.findall(r"\n\d+\.\n(.+?)\n\d,\d{3} x", raw_text)
print("Products:")
for product in products:
    print("-", product)

# 3. Extract total amount
total_match = re.search(r"ИТОГО:\n([\d ]*,\d{2})", raw_text)
total_amount = total_match.group(1) if total_match else None
print("Total:", total_amount)

# 4. Extract date and time
datetime_match = re.search(r"Время:\s*([\d.]+\s+[\d:]+)", raw_text)
date_time = datetime_match.group(1) if datetime_match else None
print("Date and time:", date_time)

# 5. Extract payment method
payment_match = re.search(r"(Банковская карта|Наличные)", raw_text)
payment_method = payment_match.group(1) if payment_match else None
print("Payment method:", payment_method)

# 6. Structured output
receipt_data = {
    "products": products,
    "all_prices": prices,
    "total_amount": total_amount,
    "date_time": date_time,
    "payment_method": payment_method
}

print("\nStructured JSON output:")
print(json.dumps(receipt_data, ensure_ascii=False, indent=2))