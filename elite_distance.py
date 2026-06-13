import requests
import math
import sys


def get_system_coords(system_name):
    url = "https://www.edsm.net/api-v1/system"
    params = {
        "systemName": system_name,
        "showCoordinates": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if not data or "coords" not in data:
        raise ValueError(f"System '{system_name}' not found or has no coordinates.")

    return data["coords"]


def calculate_distance(coords1, coords2):
    dx = coords1["x"] - coords2["x"]
    dy = coords1["y"] - coords2["y"]
    dz = coords1["z"] - coords2["z"]
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python elite_distance.py <system1> <system2>")
        print("Example: python elite_distance.py Arexe Sol")
        sys.exit(1)

    system1 = sys.argv[1]
    system2 = sys.argv[2]

    try:
        print(f"Fetching coordinates for '{system1}'...")
        coords1 = get_system_coords(system1)

        print(f"Fetching coordinates for '{system2}'...")
        coords2 = get_system_coords(system2)

        distance = calculate_distance(coords1, coords2)
        print(f"\n{distance:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except requests.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)