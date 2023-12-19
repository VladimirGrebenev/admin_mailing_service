import React from "react"
import {Link} from "react-router-dom";

const DispatchItem = ({dispatch, delete_dispatch}) => {
    return (
        <tr>
            <td>
                <Link to={`dispatches/${dispatch.uu_id}`}>{dispatch.uu_id}</Link>
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

const DispatchesList = ({dispatches, delete_dispatch}) => {
    return (
        <div className="section is-medium">
            <p className="title">
                Рассылки
            </p>
            <p className="subtitle">
                таблица созданных рассылок
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>Уникальный номер</th>
                <th>Старт</th>
                <th>Финиш</th>
                <th>Сообщение</th>
                <th>Фильтр тег</th>
                <th>Фильтр код оператора</th>
                <th></th>
                </thead>
                {dispatches.map((dispatch) => <DispatchItem dispatch={dispatch} delete_dispatch={delete_dispatch}/>)}
            </table>
            <Link class='button is-light' to='/dispatches/create'>Создать рассылку</Link>
        </div>
    )
}

export default DispatchesList;