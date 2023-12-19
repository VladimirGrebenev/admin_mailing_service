import React from "react"
import {Link, useParams} from "react-router-dom";

const DispatchItem = ({dispatch, delete_dispatch}) => {
    return (
        <tr>
            <td>
                <Link to={`dispatch/${dispatch.uu_id}`}>{dispatch.uu_id}</Link>
            </td>
            <td>{dispatch.start_datetime}</td>
            <td>{dispatch.end_datetime}</td>
            <td>{dispatch.message_text}</td>
            <td>{dispatch.tag_filter}</td>
            <td>{dispatch.operator_code_filter}</td>
            <td><button class='button is-danger' type='button'
                        onClick={()=>delete_dispatch(dispatch.uu_id)}>Удалить</button></td>
        </tr>
    )
}

const ClientDispatches = ({clients, dispatches}) => {
    const params = useParams();
    const filtered_client = clients.find((client) => client.uu_id === params.uu_id);
    const filtered_client_phone_number = filtered_client?.phone_number;
    const filtered_dispatches = dispatches.filter((dispatch) => dispatch.clients.includes(filtered_client?.uu_id))
    return (
        <div className="section is-medium">
            <p className="title">
                Рассылки клиента с номером телефона {filtered_client_phone_number}
            </p>
            <p className="subtitle">
                таблица рассылок клиента с номером {filtered_client_phone_number}
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                    <th>Старт рассылки</th>
                    <th>Конец рассылки</th>
                    <th>Сообщение</th>
                    <th>Тег</th>
                    <th>Код оператора</th>
                </thead>
                {filtered_dispatches.map((dispatch) => <DispatchItem dispatch={dispatch}/>)}
            </table>
        </div>
    )
}

export default ClientDispatches;