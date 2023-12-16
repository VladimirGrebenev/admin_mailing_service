import React from "react"
import {Link, useParams} from "react-router-dom"

const MessageItem = ({message}) => {
    return (
        <tr>
            <td>{message.client.phone_number}</td>
            <td>{message.send_status}</td>
            <td>{message.dispatch.start_datetime}</td>
            <td>{message.dispatch.end_datetime}</td>
        </tr>
    )
}

const DispatchDetails = ({dispatches, messages}) => {
    const params = useParams();
    const filtered_dispatch = dispatches.find((dispatch) => dispatch.uu_id === params.uu_id);
    const filtered_messages = messages.filter((message) => message.dispatch === filtered_dispatch?.uu_id);
    return (
        <div className="section is-medium">
            <p className="title">
                Список сообщений рассылки: {filtered_dispatch?.uu_id}
            </p>
            <p className="subtitle">
                таблица созданных сообщений
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>Номер клиента</th>
                <th>Статус отправки</th>
                <th>Старт рассылки</th>
                <th>Финиш рассылки</th>
                </thead>
                {filtered_messages.map((message)=> <MessageItem message={message}/>)}
            </table>
            <Link class='button is-light' to='/dispatches/create'>Создать рассылку</Link>
        </div>
    )
}

export default DispatchDetails