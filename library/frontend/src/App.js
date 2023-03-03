import React from 'react';
//import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import axios from 'axios';
import Header from './components/header';
import Footer from './components/footer';
import UserList from './components/User';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'users': []
        }
    }

componentDidMount() {
    // Для того, чтобы получить данные о пользователях, нужно изменить в ссылке с authors на users
    // То есть axios.get('http://127.0.0.1:8000/api/users')
    axios.get('http://127.0.0.1:8000/api/authors')
      .then(response => {
        const authors = response.data
          this.setState(
            {
                'authors': authors
            }
          )
      }).catch(error => console.log(error))
      axios.get('http://127.0.0.1:8000/api/users')
      .then(response => {
        const users = response.data
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error))
  }

render () {
    return (
      <div>
        <Header/>
        <AuthorList authors={this.state.authors} />
        <UserList users={this.state.users} />
        <Footer/>
      </div>
    )
  }

}

export default App;
