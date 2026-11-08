
import requests
import aiohttp
import asyncio
import time

# API-ის მისამართი
BASE_URL = "https://jsonplaceholder.typicode.com/todos/"

# 10 ჩანაწერის მისამართები
urls = [f"{BASE_URL}{i}" for i in range(1, 11)]


# 1. სინქრონული მოთხოვნები requests და for ციკლით
def synchronous_requests():
    results = []

    start_time = time.time()

    for url in urls:
        response = requests.get(url)
        response.raise_for_status()
        results.append(response.json())

    end_time = time.time()

    return results, end_time - start_time


# 2. ასინქრონული მოთხოვნები aiohttp და asyncio.gather-ით
async def fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def asynchronous_requests():
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[fetch(session, url) for url in urls]
        )

    end_time = time.time()

    return results, end_time - start_time


# 3. პროგრამის გაშვება
def main():
    # სინქრონული შესრულება
    sync_results, sync_time = synchronous_requests()

    print("სინქრონული შესრულება:")
    print(f"მიღებულია ჩანაწერი: {len(sync_results)}")
    print(f"დრო: {sync_time:.4f} წამი")

    print("-" * 40)

    # ასინქრონული შესრულება
    async_results, async_time = asyncio.run(
        asynchronous_requests()
    )

    print("ასინქრონული შესრულება:")
    print(f"მიღებულია ჩანაწერი: {len(async_results)}")
    print(f"დრო: {async_time:.4f} წამი")

    print("-" * 40)

    # შესრულების დროების შედარება
    difference = sync_time - async_time

    if difference > 0:
        print(
            f"ასინქრონულმა ვერსიამ {difference:.4f} "
            "წამით უფრო სწრაფად იმუშავა!"
        )
    elif difference < 0:
        print(
            f"სინქრონულმა ვერსიამ {-difference:.4f} "
            "წამით უფრო სწრაფად იმუშავა!"
        )
    else:
        print("ორივე ვერსიამ ერთნაირი დრო მოანდომა!")


if __name__ == "__main__":
    main()
