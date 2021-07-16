from datetime import datetime
from tkinter import StringVar
from sqlalchemy.sql.expression import false
from db import base
from sqlalchemy import Column, Integer, String


class user(base):
    __tablename__="user"

    id=Column(Integer, primary_key=True)
    email=Column(String, nullable=False)
    contraseña=Column(String, nullable=False)
    fecha_creacion=Column(String, nullable=False)
    def __init__(self, email, contraseña, fecha_creacion):
        self.email=email
        self.contraseña=contraseña
        self.fecha_creacion=fecha_creacion

    def __repr__(self) -> str:
        return f"Usuario, email: {self.email} fecha: {self.fecha_creacion} contraseña: {self.contraseña}"

    def __str__(self):
        return self.email