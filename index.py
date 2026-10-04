import os
import sys

# บังคับให้ Python มองเห็นโฟลเดอร์ amz และดึงข้อมูลโมดูลภายในได้ถูกต้อง
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "amz"))

from amz.main import app
