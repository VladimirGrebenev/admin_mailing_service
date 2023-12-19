import React from "react"
import {Link} from "react-router-dom";

const ClientItem = ({client, delete_client}) => {
    return (
        <tr>
            <td>
                <Link to={`clients/${client.uu_id}`}>{client.phone_number}</Link>
            </td>
            <td>{client.operator_code}</td>
            <td>{client.tag}</td>
            <td>{client.timezone}</td>
            <td><button class='button is-danger' type='button'
                        onClick={()=>delete_client(client.uu_id)}>Удалить</button></td>
        </tr>
    )
}

const ClientsList = ({clients, delete_client}) => {
    return (
        <div className="section is-medium">
            <p className="title">
                Клиенты
            </p>
            <p className="subtitle">
                таблица созданных клиентов
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>Телефон</th>
                <th>Код оператора</th>
                <th>Тег</th>
                <th>Часовой пояс</th>
                <th></th>
                </thead>
                {clients.map((client) => <ClientItem client={client} delete_client={delete_client}/>)}
            </table>
            <Link class='button is-light' to='/clients/create'>Создать клиента</Link>
        </div>
    )
}

export default ClientsList