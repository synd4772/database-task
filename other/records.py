import asyncio
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

from other.managment import *

class Record(object):
  table: SQLHTable

  def add(self):
    lst = self.get_list()
    if lst is not None:
      self.table.add_record(lst)

  def get_list(self):
    return None

class Status(Record):
  table = status_table

  def __init__(self, name:str):
    self.name = name

  def get_list(self):
    return [self.name]

class Guild(Record):
  table = guilds_table

  def __init__(self, d_guild_id:str, status_id:int):
    self.d_guild_id = d_guild_id
    self.status_id = status_id

  def get_list(self):
    return [self.d_guild_id, self.status_id]

class LogChannel(Record):
  table = log_channels_table

  def __init__(self, d_channel_id:str, guild_id:int):
    self.d_channel_id = d_channel_id
    self.guild_id = guild_id

  def get_list(self):
    return [self.d_channel_id, self.guild_id]

class PermissionStatuses(Record):
  table = permissions_statuses_table

  def __init__(self, name:str):
    self.name = name

  def get_list(self):
    return [self.name]

class Permissions(Record):
  table = permissions_table

  def __init__(self, name:str, permission_statuses_id:int, permission_guild_id:int | str):
    self.name = name
    self.permission_statuses_id = permission_statuses_id
    self.permission_guild_id = permission_guild_id

  def get_list(self):
    return [self.name, self.permission_statuses_id, self.permission_guild_id]

class Commands(Record):
  table = commands_table

  def __init__(self, name:str):
    self.name = name

  def get_list(self):
    return [self.name]

class CommandPermissions(Record):
  table = command_permissions_table

  def __init__(self, guild_id:int, permission_id:int, command_id:int):
    self.guild_id = guild_id
    self.permission_id = permission_id
    self.command_id = command_id

  def get_list(self):
    return [self.guild_id, self.permission_id, self.command_id]

class Roles(Record):
  table = roles_table

  def __init__(self, d_role_id:str, guild_id:int):
    self.d_role_id = d_role_id
    self.guild_id = guild_id

  def get_list(self):
    return [self.d_role_id, self.guild_id]

class GuildMembers(Record):
  table = guild_members_table

  def __init__(self, d_member_id:str, value:int, guild_id:int):
    self.d_member_id = d_member_id
    self.value = value
    self.guild_id = guild_id

  def get_list(self):
    return [self.d_member_id, self.value, self.guild_id]



class RolePermissions(Record):
  table = role_permissions_table

  def __init__(self, role_id:int, permission_id:int):
    self.role_id = role_id
    self.permission_id = permission_id

  def get_list(self):
    return [self.role_id, self.permission_id]

class MemberPermissions(Record):
  table = member_permissions_table

  def __init__(self, member_id:int, permission_id:int):
    self.member_id = member_id
    self.permission_id = permission_id

  def get_list(self):
    return [self.member_id, self.permission_id]

class ItemTypes(Record):
  table = item_types_table

  def __init__(self, name:str):
    self.name = name

  def get_list(self):
    return [self.name]

class Items(Record):
  table = items_table

  def __init__(self, name:str, type_id:int):
    self.name = name
    self.type_id = type_id

  def get_list(self):
    return [self.name, self.type_id]

class Prices(Record):
  table = prices_table

  def __init__(self, item_id:int, price:int):
    self.item_id = item_id
    self.price = price

  def get_list(self):
    return [self.item_id, self.price]

class MemberItems(Record):
  table = prices_table

  def __init__(self, item_id:int, member_id:int):
    self.item_id = item_id
    self.member_id = member_id

  def get_list(self):
    return [self.item_id, self.member_id]

if __name__ == "__main__":

  pass