club_members = {"Olamide", "Aisha", "John", "Philips"}

print("original members")
print(club_members)

 #Add one member
club_members.add("Amao")

# Add multiple members
club_members.update(["peter", "Fatima"])

# Remove one member
club_members.remove("Aisha")

print("\nUpdated Members:")
print(club_members)

print("\nTotal Members:", len(club_members))

#tracking attendees at a workshop.
attendees = {"Olamide", "Grace"}

# Late registration
attendees.add("David")

# Someone cancels
attendees.discard("Grace")

print(attendees)
