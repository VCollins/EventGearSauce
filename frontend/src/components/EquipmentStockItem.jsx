import React from "react";

function EquipmentStockItem({ equipmentStockItem, onDelete }) {
    //const formattedDate = new Date(equipmentStockItem.created_at).toLocaleDateString("en-US")

    return (
        <div className="equipmentStockItem-container">
            <p className="equipmentStockItem-manufacturer">{equipmentStockItem.manufacturer}</p>
            <p className="equipmentStockItem-model_name">{equipmentStockItem.model_name}</p>
            <p className="equipmentStockItem-description">{equipmentStockItem.description}</p>
            <p className="equipmentStockItem-serial_number">{equipmentStockItem.serial_number}</p>
            <p className="equipmentStockItem-amount_available">{equipmentStockItem.amount_available}</p>
            <p className="equipmentStockItem-rental_cost">{equipmentStockItem.rental_cost}</p>
            <button className="delete-button" onClick={() => onDelete(equipmentstockitem.id)}>
                Delete
            </button>
        </div>
    );    
}

export default EquipmentStockItem