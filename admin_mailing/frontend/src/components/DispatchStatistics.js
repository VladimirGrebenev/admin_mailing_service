import React from "react";
import {Link} from "react-router-dom";

const StatItem = ({dispatch, messages}) => {

    const filtered_messages = messages.filter((message) => message.dispatch === dispatch.uu_id);
    console.log(filtered_messages)
    const filtered_messages_send = filtered_messages.filter((message) => message.send_status === true);
    console.log(filtered_messages_send)
    return (
        <tr>
            <td>
                <Link
                    to={`dispatches/${dispatch.uu_id}`}>{dispatch.uu_id}</Link>
            </td>
            <td>{dispatch.start_datetime}</td>
            <td>{dispatch.end_datetime}</td>
            <td>{filtered_messages.length}</td>
            <td>{filtered_messages_send.length}</td>
        </tr>
    )
}

const DispatchStatistics = ({dispatches, messages}) => {

    return (
        <div className="section is-medium">
            <p className="title">
                Статистика рассылок
            </p>
            <p className="subtitle">
                таблица статистики рассылок
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>uu_id рассылки</th>
                <th>Старт</th>
                <th>Финиш</th>
                <th>Всего сообщений</th>
                <th>Отправлено сообщений</th>
                <th></th>
                </thead>
                {dispatches.map((dispatch) => <StatItem dispatch={dispatch} messages={messages} />)}
            </table>
            <Link class='button is-light' to='/dispatches/create'>Создать
                рассылку</Link>
        </div>
    )
}

export default DispatchStatistics;