"""
Club Meets will have a login page where users can sign in using their account credentials. The application will
distinguish between two types of users: club executives and regular members. Based on the user’s role, they will
be directed to an interface with different permissions. Executives will have access to administrative features.
This includes viewing attendance records for all members and reviewing overall club participation. Members will
have access to their personal attendance records, allowing them to see which events they have attended and track
their participation. This role-based login system will ensure that users can only access features that are relevant
to their responsibilities.
"""
# Demi -  Login page (re-routes differently for members vs executives) - goes to separate page with buttons/sections
# # for different actions if you are member or executive

import tkinter as tk

