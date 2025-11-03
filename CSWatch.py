from requests import get, post

BASE_URL = "https://cswatch.in/api"
SEARCH_PATH = "/players/search"
PLAYERS_PATH = "/players"

class CSWatch:
    def __init__(self):
        self.search_path = BASE_URL + SEARCH_PATH
        self.players_path = BASE_URL + PLAYERS_PATH

    def resolve_player_id(self, player_name: str) -> str | None:
        payload = {"query": player_name}
        r = post(self.search_path, json=payload)
        if r.status_code != 200:
            return None
        data = r.json()
        if not data["success"]:
            return None
        return data["redirectUrl"].split("/")[-1]

    def get_trust_score(self, player_id: str) -> int | None:
        if "https://" in player_id:
            player_id = player_id.rstrip("/").split("/")[-1]
        if not player_id.isdigit():
            player_id = self.resolve_player_id(player_id)
        if not player_id:
            return None
        r = get(f"{self.players_path}/{player_id}")
        if r.status_code != 200:
            return None
        data = r.json()
        cswatch = data.get("csWatchAnalysis", {}).get("totalScore", 0)
        return int(cswatch)
