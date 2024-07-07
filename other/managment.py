import asyncio
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))

if root_dir not in sys.path:
    sys.path.append(root_dir)

from other.sqlite_handler import *

def add_columns(table:SQLHTable, columns:list):
  for column in columns:
    table.add_column(column)

def set_tables(database_instance:SQLHDatabase, tables:list):
    for table in tables:
        database_instance.add_table(table)

status_table = SQLHTable(name="status", row_id=True, row_id_name="id")
status_name = SQLHColumn(name="name", type="TEXT", constraint="NOT NULL")
add_columns(status_table, [status_name])

guilds_table = SQLHTable(name="guilds", row_id = True, row_id_name="id")
guilds_d_guild_id = SQLHColumn(name="d_guild_id", type="TEXT", constraint="NOT NULL")
guilds_status = SQLHColumn(name="status_id", type="INTEGER", constraint="NOT NULL", foreign_key=status_table)
add_columns(guilds_table, [guilds_d_guild_id, guilds_status])

log_channels_table = SQLHTable(name="log_channels", row_id=True, row_id_name="id")
log_channels_d_channel_id = SQLHColumn(name="d_channel_id", type="TEXT", constraint="NOT NULL")
log_channels_guild_id = SQLHColumn(name="guild_id", type="INTEGER", constraint="NOT NULL")
add_columns(log_channels_table, [log_channels_d_channel_id, log_channels_guild_id])

permissions_statuses_table = SQLHTable(name="permissions_statuses", row_id=True, row_id_name="id")
permissions_statuses_name = SQLHColumn(name="name", type="TEXT")
add_columns(permissions_statuses_table, [permissions_statuses_name])

permissions_table = SQLHTable(name="permissions", row_id=True, row_id_name="id")
permission_name = SQLHColumn(name="name", type="TEXT", constraint="NOT NULL")
permission_statuses_id = SQLHColumn(name="permission_statuses_id", type="INTEGER", constraint="NOT NULL")
permission_guild_id = SQLHColumn(name="guild_id", type="INTEGER", constraint="NULL", foreign_key=guilds_table)
add_columns(permissions_table, [permission_name, permission_statuses_id, permission_guild_id])

commands_table = SQLHTable(name="commands", row_id=True, row_id_name="id")
commands_name = SQLHColumn(name="name", type="TEXT")
add_columns(commands_table, [commands_name])

command_permissions_table = SQLHTable(name="command_permissions", row_id=True, row_id_name="id")
command_permissions_guild_id = SQLHColumn(name="guild_id", type="INTEGER", constraint="NOT NULL", foreign_key=guilds_table)
command_permissions_permission_id = SQLHColumn(name="permission_id", type="INTEGER", foreign_key=permissions_table)
command_permissions_command_id = SQLHColumn(name="command_id", type="INTEGER", foreign_key=commands_table)
add_columns(command_permissions_table, [command_permissions_guild_id, command_permissions_permission_id, command_permissions_command_id])

roles_table = SQLHTable(name="roles", row_id=True, row_id_name="id")
roles_d_role_id = SQLHColumn(name="d_role_id", type="TEXT", constraint="NOT NULL")
roles_guild_id = SQLHColumn(name="guild_id", type="INTEGER", constraint="NOT NULL", foreign_key=guilds_table)
add_columns(roles_table, [roles_d_role_id, roles_guild_id])

guild_members_table = SQLHTable(name="guild_members", row_id=True, row_id_name="id")
guild_members_d_member_id = SQLHColumn(name="d_member_id", type="TEXT", constraint="NOT NULL")
guild_members_value = SQLHColumn(name="value", type="INTEGER", constraint="NOT NULL")
guild_members_guild_id = SQLHColumn(name="guild_id", type="INTEGER", constraint="NOT NULL", foreign_key=guilds_table)
add_columns(guild_members_table, [guild_members_d_member_id,guild_members_value,guild_members_guild_id])

role_permissions_table = SQLHTable(name="role_permissions", row_id=True, row_id_name="id")
role_permissions_role_id = SQLHColumn(name="role_id", type="INTEGER", constraint="NOT NULL", foreign_key=roles_table)
role_permissions_permission_id = SQLHColumn(name="permission_id", type="INTEGER", constraint="NOT NULL", foreign_key=permissions_table)
add_columns(role_permissions_table, [role_permissions_role_id, role_permissions_permission_id])

member_permissions_table = SQLHTable(name="member_permissions", row_id=True, row_id_name="id")
member_permissions_member_id = SQLHColumn(name="member_id", type="INTEGER", constraint="NOT NULL", foreign_key=guild_members_table)
member_permissions_permission_id = SQLHColumn(name="permission_id", type="INTEGER", foreign_key=permissions_table)
add_columns(member_permissions_table, [member_permissions_member_id])

item_types_table = SQLHTable(name="item_types", row_id=True, row_id_name="id")
item_types_type = SQLHColumn(name="name", type="TEXT", constraint="NOT NULL")
add_columns(item_types_table, [item_types_type])

items_table = SQLHTable(name="items", row_id=True, row_id_name="id")
items_item = SQLHColumn(name="name", type="INTEGER", constraint="NOT NULL")
items_type_id = SQLHColumn(name="type_id", type="INTEGER", constraint="NOT NULL", foreign_key=item_types_table)
add_columns(items_table, [items_item, items_type_id])

prices_table = SQLHTable(name="prices", row_id=True, row_id_name="id")
prices_item_id = SQLHColumn(name="item_id", type="INTEGER", constraint="NOT NULL", foreign_key=items_table)
prices_price = SQLHColumn(name="price", type="INTEGER", constraint="NOT NULL")
add_columns(prices_table, [prices_item_id, prices_price])

member_items_table = SQLHTable(name="member_items", row_id=True, row_id_name="id")
member_items_item_id = SQLHColumn(name="item_id", type="INTEGER", constraint="NOT NULL", foreign_key=items_table)
member_items_member_id = SQLHColumn(name="member_id", type="INTEGER", constraint="NOT NULL", foreign_key=guild_members_table)
add_columns(member_items_table, [member_items_item_id, member_items_member_id])

main_dtbs_tables = [
  status_table,
  guilds_table,
  log_channels_table,
  permissions_statuses_table,
  permissions_table,
  commands_table,
  command_permissions_table,
  roles_table,
  guild_members_table,
  role_permissions_table,
  member_permissions_table,
  item_types_table,
  items_table,
  prices_table,
  member_items_table
  ]
set_tables(main_dtbs, main_dtbs_tables)






