import React from 'react'

class DispatchForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {start_datetime: '2023-12-16T10:12', end_datetime: '2023-12-16T10:12',
         message_text: '', tag_filter: '', operator_code_filter: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createDispatch(this.state.start_datetime, this.state
        .end_datetime, this.state.message_text, this.state.tag_filter,
         this.state.operator_code_filter)
        event.preventDefault()
    }

    render() {
        return (
            <div className="section">
                <div className="columns">
                    <div className="column"></div>
                    <div className="column is-one-third">
                        <form onSubmit={(event) => this.handleSubmit(event)}>
                            <div className="field">
                                <label className="label">Старт рассылки</label>
                                <div className="control">
                                    <input name="start_datetime" className="input"
                                        type="text" placeholder="старт рассылки 2023-12-16T10:12"
                                           value={this.state.start_datetime}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Финиш рассылки</label>
                                <div className="control">
                                    <input name="end_datetime"
                                    className="input" type="text"
                                    placeholder="финиш рассылки 2023-12-16T10:12"
                                           value={this.state.end_datetime}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Сообщение</label>
                                <div className="control">
                                    <input name="message_text"
                                    className="input" type="text"
                                    placeholder="сообщение"
                                           value={this.state.message_text}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Тег фильтр</label>
                                <div className="control">
                                    <input name="tag_filter"
                                    className="input" type="text"
                                    placeholder="тег фильтр"
                                           value={this.state.tag_filter}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Код оператора фильтр</label>
                                <div className="control">
                                    <input name="operator_code_filter"
                                    className="input" type="text"
                                    placeholder="код оператора фильтр"
                                           value={this.state.operator_code_filter}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <input className="button is-success" type="submit" value="Создать"/>
                            </div>
                        </form>
                    </div>
                    <div className="column"></div>
                </div>
            </div>
        );
    }
}

export default DispatchForm;