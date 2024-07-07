from other.records import *

# Чтобы делать sql запросы, нужно использовать main_dtbs.execute_query("") , может вернуть None или пустой список в случае того, если ничего не найдено.
# Можно работать не только через запросы, но через классы, в моем модуле sqlite-handler в классе SQLHTable можно увидеть какие есть методы. Но вообще лучше пока-что не стоит, модуль я не дописал.

def get_guilds(d_member_id: str) -> list: # ( ДОПОЛНИТЕЛЬНЫЕ АРГУМЕНТЫ НЕ ДОБАВЛЯТЬ )
  # эта функция прежде всего должна узнать есть ли участник в базе данных,
  member_id = main_dtbs.execute_query(f'SELECT id FROM guild_members  WHERE d_member_id = "{d_member_id}"')
  if not member_id:
        print("нет такого бро")
        return False
  # если да, то ищет дискордный айди дискорд сервера в котором он находится ( нужно учитывать то, что пользователь может находится
  # на разных серверах )
  member_id = member_id[0][0]

  guild_id = main_dtbs.execute_query(f'SELECT id FROM guilds WHERE d_guild_id =  "{member.guild.id}" ')
  DD_guild_id = main_dtbs.execute_query(f'SELECT d_guild_id FROM guilds WHERE id = "{guild_id}"')
  if not guild_id :
    print("бож такого сервера нет")
    return None
  # N.B. ЕСЛИ СЕРВЕР БУДЕТ НЕ НАЙДЕН, ТО НУЖНО ВОЗВРАЩАТЬ "None"
  guild_ids = [elm[0] for elm in DD_guild_id]

  return guild_ids # вернуть нужно дискордный айди дискорд сервера в виде списка

def get_permissions(d_member_id: str) -> list: # ( ДОПОЛНИТЕЛЬНЫЕ АРГУМЕНТЫ НЕ ДОБАВЛЯТЬ )
  guild_members_id = main_dtbs.execute_query(f'SELECT id FROM guild_members WHERE d_member_id = "{d_member_id}"')
  if not guild_members_id:
    return []
  guild_members_id = guild_members_id[0][0]

  member_permissions_id = main_dtbs.execute_query(f'SELECT permission_id FROM member_permissions WHERE member_id = "{guild_members_id}"')
  if not member_permissions_id:
    return []
  lst_member_permissions_ids = [elm[0] for elm in member_permissions_id]

  member_permissions = main_dtbs.execute_query(f'SELECT name FROM permissions WHERE permission_id = "{member_permissions_id}" ')
  lst_permissions = [name[0] for name in member_permissions]
  return lst_permissions

  # эта функция должна возвращать список прав пользователя из базы данных. И именно список.
  # если нету прав , возвращается пустой список


def get_commands_by_permissions(permission_id: int | list, guild_id: int) -> list: # ( ДОПОЛНИТЕЛЬНЫЕ АРГУМЕНТЫ НЕ ДОБАВЛЯТЬ )
  # эта функция будет возвращать все команды доступные по праву, а тоесть permission_id ( это если что индекс записи в таблице permissions )
  # если нету команд, возвращается пустой список
  # N.B. АРГУМЕНТ permission_id МОЖЕТ ИМЕТЬ ЛИБО СПИСОК, ЛИБО ЧИСЛО, А ТОЕСТЬ НУЖНО БУДЕТ СДЕЛАТЬ ПРОВЕРКУ НА ЭТО (isinstance(permission_id, list))
  return


if __name__ == "__main__":
  list_of_members = ["742340558504198165", "1236714340569321574", "703722066771443816", "536995329434714112", "604390737177608202"] # список участников ( дискорд айди )
  print("Цикл начался\n")
  for member in list_of_members: # цикл нужен только для того, чтобы по очередной проверять участников.
    guild: str | list = find_guild(member) # вызов функции ( ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ НЕ ДОБАВЛЯТЬ. )

    if guild is not None: # проверка на то, есть ли вообще на каком - то сервере участник
      print(f"Участник с айди \"{member}\" находится на сервере под айди \"{guild[0]}\"" if len(guild) == 1 else f"Участник с айди \"{member}\" находится на серверах под айди \"{', '.join([str(i) for i in guild])}\"") # обычный вывод
    else:
      print(f"У участника с айди \"{member}\" нет серверов.")

    permissions: list = get_permissions(member)
    commands: list = []
    if permissions is not None and len(permissions) : # проверка на то, есть ли в списке что-то
      commands = get_commands_by_permissions(permissions)
      print(f"У участника с айди \"{member}\" есть следующие права - \"{", ".join(permissions)}\"")
    else:
      print(f"У участника с айди \"{member}\" нет прав.")

    if commands is not None and len(commands):
      print(f"У участника с айди \"{member}\" досутпны следующие команды - \"{", ".join(commands)}\"")
    else:
      print(f"У участника с айди \"{member}\" нет доступных команд.")
    print()
  else:
    print("Цикл завершен")
