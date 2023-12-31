import React from "react"
import {Link, useParams} from "react-router-dom";

const DispatchItem = ({dispatch}) => {
    return (
        <tr>
            <td>{dispatch.uu_id}</td>
            <td>{dispatch.start_datetime}</td>
            <td>{dispatch.end_datetime}</td>
            <td>{dispatch.message_text}</td>
            <td>{dispatch.tag_filter}</td>
            <td>{dispatch.operator_code_filter}</td>
        </tr>
    )
}

const ClientDispatches = ({clients, dispatches}) => {
    const params = useParams();
    const filtered_client = clients.find((client) => client.uu_id === params.uu_id);
    const filtered_client_phone_number = filtered_client?.phone_number;
    const filtered_dispatches = dispatches.filter((dispatch) => {
        if (dispatch.tag_filter && dispatch.operator_code_filter) {
            return dispatch.tag_filter === filtered_client?.tag && dispatch.operator_code_filter === filtered_client?.operator_code;
        } else if (dispatch.tag_filter) {
            return dispatch.tag_filter === filtered_client?.tag;
        } else if (dispatch.operator_code_filter) {
            return dispatch.operator_code_filter === filtered_client?.operator_code;
        }
        return false;
    });
    return (
        <div className="section is-medium">
            <p className="title">
                Рассылки клиента с номером
                телефона {filtered_client_phone_number}
            </p>
            <p className="subtitle">
                таблица рассылок клиента с
                номером {filtered_client_phone_number}
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>uu_id рассылки</th>
                <th>Старт рассылки</th>
                <th>Конец рассылки</th>
                <th>Сообщение</th>
                <th>Тег</th>
                <th>Код оператора</th>
                </thead>
                {filtered_dispatches.map((dispatch) => <DispatchItem
                    dispatch={dispatch}/>)}
            </table>
            <Link class='button is-light' to='/dispatches/create'>Создать
                рассылку</Link>
        </div>
    )
}

export default ClientDispatches;