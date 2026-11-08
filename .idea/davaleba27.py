
import asyncio
import aiohttp


async def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:

                response.raise_for_status()

                # მონაცემების ასინქრონულად მიღება
                posts = await response.json()

                # პირველი 20 პოსტის აღება
                first_20_posts = posts[:20]

                # მხოლოდ userId == 1 პოსტების გაფილტვრა
                filtered_posts = [
                    post for post in first_20_posts
                    if post["userId"] == 1
                ]

                # მხოლოდ სათაურების გამოტანა
                print("შერჩეული პოსტების სათაურები:\n")

                for index, post in enumerate(filtered_posts, start=1):
                    print(f"{index}. {post['title']}")

    except aiohttp.ClientError as error:
        print("შეცდომა API-სთან დაკავშირებისას:", error)


# ასინქრონული ფუნქციის გაშვება
asyncio.run(get_posts())
