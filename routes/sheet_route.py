from controllers import sheet_control
from fastapi import APIRouter
from typing import List, Dict, Any

router = APIRouter()

router.add_api_route("/create_csv", endpoint=sheet_control.create_csv_control, methods=["POST"], response_model=dict)
router.add_api_route("/upload_csv", endpoint=sheet_control.upload_csv_control, methods=["POST"], response_model=dict)
router.add_api_route("/insert_mongo", endpoint=sheet_control.mongo_insert_control, methods=["POST"], response_model=dict)
router.add_api_route("/fetch_mongo", endpoint=sheet_control.mongo_read_control, methods=["GET"], response_model=dict)
router.add_api_route("/insert_food", endpoint=sheet_control.mongo_food_insert_control, methods=["POST"], response_model=dict)
router.add_api_route("/get_food", endpoint=sheet_control.mongo_food_get_control, methods=["GET"], response_model=List[Dict[str, Any]])