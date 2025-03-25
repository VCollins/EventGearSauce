import React from "react";

function Quotation({ quotation, onDelete }) {
    const formattedDate = new Date(quotation.date_created).toLocaleDateString("en-US")

    return (
        <div className="quotation-container">
            <p className="quotation-quote_number">{quotation.quote_number}</p>
            <p className="quotation-date_created">{formattedDate}</p>
            <p className="quotation-client">{quotation.client}</p>
            <p className="quotation-equipment">{quotation.equipment}</p>
            <p className="quotation-total_quote_amount">{quotation.total_quote_amount}</p>
            <button className="delete-button" onClick={() => onDelete(equipmentstockitem.id)}>
                Delete
            </button>
        </div>
    );    
}

export default Quotation