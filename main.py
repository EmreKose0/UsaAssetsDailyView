import Get_Assets_List
import Get_Assets_Price_Daily

async def get_assets_list():
    Get_Assets_List.fetch_and_insert_assets()

async def get_Assets_Price_Daily():
    Get_Assets_Price_Daily.fetch_and_insert_assets_prices()

async def main():
    await get_assets_list()
    await get_Assets_Price_Daily()

