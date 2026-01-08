from datetime import datetime

notices = []

# ---------- Owner: Base Notice Board ----------
def show_menu():
    print("\n===== Digital Notices Board =====")
    print("1. Add Notices")
    print("2. View Notices")
    print("3. Search Notices")
    print("4. Delete Expired Notices")
    print("5. Exit")

# ---------- Member 1: Add Notice ----------
def add_notice():
    title = input("Enter title of notice: ")
    content = input("Enter content of notice: ")
    expiry = input("Enter expiry date (YYYY-MM-DD): ")

    try:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format")
        return

    notices.append({
        "title": title,
        "content": content,
        "expiry": expiry_date
    })
    print("Notice added successfully")

# ---------- Member 2: View Notices ----------
def view_notices():
    if not notices:
        print("No notices available")
        return

    print("\n--- Active Notices ---")
    today = datetime.today().date()

    for n in notices:
        status = "EXPIRED" if n["expiry"] < today else "ACTIVE"
        print(f"\nTitle   : {n['title']}")
        print(f"Content : {n['content']}")
        print(f"Expiry  : {n['expiry']} ({status})")

# ---------- Member 3: Search Notice ----------
def search_notice():
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for n in notices:
        if keyword in n["title"].lower() or keyword in n["content"].lower():
            print(f"\nTitle   : {n['title']}")
            print(f"Content : {n['content']}")
            print(f"Expiry  : {n['expiry']}")
            found = True

    if not found:
        print("No matching notices found")

# ---------- Member 4: Delete Expired Notices ----------
def delete_expired_notices():
    today = datetime.today().date()
    before_count = len(notices)

    notices[:] = [n for n in notices if n["expiry"] >= today]

    deleted = before_count - len(notices)
    print(f"{deleted} expired notice(s) deleted")

# ---------- Main Loop ----------
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_notice()
    elif choice == "2":
        view_notices()
    elif choice == "3":
        search_notice()
    elif choice == "4":
        delete_expired_notices()
    elif choice == "5":
        print("Exiting Digital Notice Board System")
        break
    else:
        print("Invalid choice. Please try again.")
