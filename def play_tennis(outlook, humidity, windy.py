def play_tennis(outlook, humidity, windy):
    if outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"

    elif outlook == "Rain":
        if windy == "Strong":
            return "No"
        else:
            return "Yes"

    else:  # Overcast
        return "Yes"

# Test cases
print(play_tennis("Sunny", "High", "Weak"))      # No
print(play_tennis("Sunny", "Normal", "Weak"))    # Yes
print(play_tennis("Rain", "High", "Strong"))     # No
print(play_tennis("Overcast", "High", "Weak"))   # Yes