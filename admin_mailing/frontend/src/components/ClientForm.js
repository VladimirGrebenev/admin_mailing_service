import React from 'react'

class ClientForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {phone_number: '79834578640', operator_code: '983',
         tag: 'mts', timezone: 'GMT+03'}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createClient(this.state.phone_number,
         this.state.operator_code, this.state.tag, this.timezone)
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
                                <label className="label">Номер клиента</label>
                                <div className="control">
                                    <input name="phone_number" className="input"
                                    type="text" placeholder="номер клиента 79834578640"
                                           value={this.state.phone_number}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Код оператора</label>
                                <div className="control">
                                    <input name="operator_code"
                                    className="input" type="text"
                                    placeholder="код оператора 983"
                                           value={this.state.operator_code}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Тег</label>
                                <div className="control">
                                    <input name="tag"
                                    className="input" type="text"
                                    placeholder="произвольный тег"
                                           value={this.state.tag}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Часовой пояс</label>
                                <div className="control">
                                    <input name="timezone"
                                    className="input" type="text"
                                    placeholder="часовой пояс"
                                           value={this.state.timezoner}
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

export default ClientForm